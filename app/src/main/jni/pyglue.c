#include <jni.h>
#include <Python.h>
#include <android/log.h>

#define APPNAME "PyApp"

static PyObject *app_module = NULL;
static JNIEnv *jnienv = NULL;

// function checks for python exception
//   and deals with it (shows message to user)
// returns true on error
char check_for_exception(JNIEnv *env)
{
    PyObject *ptype, *pvalue, *ptraceback;
    PyErr_Fetch(&ptype, &pvalue, &ptraceback);
    if(ptype) {
        const char *message = "An error occured in the Python layer, thats all we know.";

        PyObject *pvalue_str = NULL;
        if(pvalue) {
            pvalue_str = PyObject_Str(pvalue);
            message = PyString_AsString(pvalue_str);
        }

        PyObject *ptraceback_str = NULL;
        PyObject *traceback = PyImport_ImportModule("traceback");
        if(traceback) {
            PyObject *name = PyString_FromString("format_exception");
            PyObject *formatted = PyObject_CallMethodObjArgs(traceback, name, ptype, pvalue, ptraceback, NULL);
            Py_DECREF(name);
            if(formatted) {
                PyObject *emptystr = PyString_FromString("");
                ptraceback_str = PyObject_CallMethod(emptystr, "join", "O", formatted);
                message = PyString_AsString(ptraceback_str);
                Py_DECREF(emptystr);
                Py_DECREF(formatted);
            }
            Py_DECREF(traceback);
        }

        jclass glue_class = (*env)->FindClass(env, "com/owner/android_game/PyGlue");
        jmethodID showalert_method = (*env)->GetStaticMethodID(env, glue_class, "showFatalAlert", "(Ljava/lang/String;)V");
        jstring message_object = (*env)->NewStringUTF(env, message);
        (*env)->CallStaticVoidMethod(env, glue_class, showalert_method, message_object);
        (*env)->DeleteLocalRef(env, message_object);

        Py_XDECREF(ptraceback_str);
        Py_XDECREF(pvalue_str);

        Py_XDECREF(ptraceback);
        Py_XDECREF(pvalue);
        Py_XDECREF(ptype);

        return 1;
    }

    return 0;
}

//TODO: meta_path importer
/*
static PyObject *meta_path_find_module(PyObject *self, PyObject *args, PyObject *kwargs)
{
    static char *kwlist[] = {"fullname", "path", NULL};

    PyObject *path;
    const char *fullname;
    if(!PyArg_ParseTupleAndKeywords(args, kwargs, "s|O:find_module", kwlist, &fullname, &path))
        return NULL;

    printf("import %s\n", fullname);

    jclass glue_class = (*jnienv)->FindClass(jnienv, "com/example/owner/pyapp/PyGlue");
    jmethodID moduleexists_method = (*jnienv)->GetStaticMethodID(jnienv, glue_class, "moduleExists", "(Ljava/lang/String;)Z");
    jstring fullname_object = (*jnienv)->NewStringUTF(jnienv, fullname);
    char exists = (*jnienv)->CallStaticBooleanMethod(jnienv, glue_class, moduleexists_method, fullname_object);
    (*jnienv)->DeleteLocalRef(jnienv, fullname_object);

    if(exists) {
        printf("found module %s\n", fullname);
        Py_INCREF(self);
        return self;
    }

    Py_RETURN_NONE;
}

static PyObject *meta_path_load_module(PyObject *self, PyObject *args, PyObject *kwargs)
{
    static char *kwlist[] = {"fullname", NULL};

    const char *fullname;
    if(!PyArg_ParseTupleAndKeywords(args, kwargs, "s:load_module", kwlist, &fullname))
        return NULL;

    printf("import %s\n", fullname);

    PyErr_SetString(PyExc_ImportError, "failed to import");
    return NULL;
}

static PyMethodDef meta_path_find_module_method = {
        "find_module",
        (PyCFunction)meta_path_find_module,
        METH_VARARGS | METH_KEYWORDS,
        NULL
};

static PyMethodDef meta_path_load_module_method = {
        "load_module",
        (PyCFunction)meta_path_load_module,
        METH_VARARGS | METH_KEYWORDS,
        NULL
};

void register_meta_path_importer()
{
    PyObject *method_dict = PyDict_New();
    PyObject *empty_tuple = PyTuple_New(0);
    PyObject *loader_name = PyString_FromString("meta_path_loader");
    PyObject *meta_path_loader = PyObject_CallFunctionObjArgs((PyObject *)&PyType_Type, loader_name, empty_tuple, method_dict, NULL);
    Py_XDECREF(loader_name);
    Py_XDECREF(empty_tuple);
    Py_XDECREF(method_dict);

    PyObject *loader_find_module = PyCFunction_New(&meta_path_find_module_method, meta_path_loader);
    PyObject_SetAttrString(meta_path_loader, "find_module", loader_find_module);
    PyObject *loader_load_module = PyCFunction_New(&meta_path_load_module_method, meta_path_loader);
    PyObject_SetAttrString(meta_path_loader, "load_module", loader_load_module);

    PyList_Insert(PySys_GetObject("meta_path"), 0, meta_path_loader);
}
*/

JNIEXPORT void JNICALL
Java_com_owner_android_1game_PyGlue_initWithHome(JNIEnv *env, jclass type, jstring home_path, jstring dynload_path, jstring app_path)
{
    jnienv = env;

    const char *home_path_cstr = (*env)->GetStringUTFChars(env, home_path, 0);
    const char *dynload_path_cstr = (*env)->GetStringUTFChars(env, dynload_path, 0);
    const char *app_path_cstr = (*env)->GetStringUTFChars(env, app_path, 0);

    freopen("/data/data/com.owner.android-game/stdout.txt", "wb", stdout);
    freopen("/data/data/com.owner.android-game/stderr.txt", "wb", stderr);

    printf("home: %s\n", home_path_cstr);
    printf("dynload: %s\n", dynload_path_cstr);

    assert(strlen(home_path_cstr) + strlen(dynload_path_cstr) + strlen(app_path_cstr) < 255);

    char path[256];
    memset(path, 0, sizeof(path));
    strcat(path, home_path_cstr);
    strcat(path, ":");
    strcat(path, dynload_path_cstr);
    strcat(path, ":");
    strcat(path, app_path_cstr);

    printf("path: %s\n", path);

    Py_NoSiteFlag = 1;
    Py_SetProgramName("programname");
    Py_SetPythonHome(".");
    Py_Initialize();
    PySys_SetPath(path);
    //register_meta_path_importer();

    PyImport_ImportModule("site");
    app_module = PyImport_ImportModule("app");
    check_for_exception(env);

    fflush(stdout);
    fflush(stderr);

    (*env)->ReleaseStringUTFChars(env, home_path, home_path_cstr);
    (*env)->ReleaseStringUTFChars(env, dynload_path, dynload_path_cstr);
    (*env)->ReleaseStringUTFChars(env, app_path, app_path_cstr);
}

JNIEXPORT void JNICALL
Java_com_owner_android_1game_PyGlue_finish(JNIEnv *env, jclass type)
{
    Py_Finalize();
}

JNIEXPORT void JNICALL
Java_com_owner_android_1game_PyGlue_callFunction(JNIEnv *env, jclass type, jstring funcName_)
{
    if(app_module == NULL)
        return;

    const char *funcName = (*env)->GetStringUTFChars(env, funcName_, 0);

    if(PyObject_HasAttrString(app_module, funcName)) {
        PyObject_CallMethod(app_module, funcName, "");
        if(check_for_exception(env)) {
            Py_DECREF(app_module);
            app_module = NULL;
        }
    }

    (*env)->ReleaseStringUTFChars(env, funcName_, funcName);
}
