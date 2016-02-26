package com.owner.android_game;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.Context;
import android.content.DialogInterface;
import android.content.res.AssetManager;
import android.util.Log;

import java.io.BufferedInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.zip.ZipEntry;
import java.util.zip.ZipInputStream;

/**
 * Created by owner on 26/02/16.
 */
public class PyGlue {
    static {
        System.loadLibrary("pyglue");
    }

    public static native void initWithHome(String homePath, String dynloadPath, String appPath);
    public static native void finish();

    public static native void callFunction(String funcName);

    //HACK: move to class instance
    public static Context currentContext = null;

    //TODO: meta_path importer
    /*
    public static boolean moduleExists(String fullname) {
        String[] parts = fullname.split("\\.");
        String submodule = parts[0];
        String module_path = TextUtils.join("/", parts);
        System.out.println(module_path);

        try {
            InputStream is = currentContext.getAssets().open("lib.zip");
            ZipInputStream zis = new ZipInputStream(new BufferedInputStream(is));

            ZipEntry zipEntry;
            while((zipEntry = zis.getNextEntry()) != null) {
                String filename = zipEntry.getName();

                if(filename.equals(module_path + ".py") ||
                        filename.equals(module_path + ".pyc") ||
                        filename.equals(module_path + "/__init__.py") ||
                        filename.equals(module_path + "/__init__.pyc") ||
                        filename.equals("lib-dynload/" + module_path + ".so")) {
                    return true;
                }
            }

            zis.close();
        } catch(IOException e) {
            // fall-through
        }

        return false;
    }
    */

    public static void showFatalAlert(final String message) {
        if(currentContext == null)
            return;

        ((Activity)currentContext).runOnUiThread(new Runnable() {
            @Override
            public void run() {
                new AlertDialog.Builder(currentContext)
                        .setTitle("PyApp")
                        .setMessage(message)
                        .setPositiveButton(android.R.string.ok, new DialogInterface.OnClickListener() {
                            public void onClick(DialogInterface dialog, int which) {
                                ((Activity) currentContext).finish();
                            }
                        })
                        .show();
            }
        });
    }

    public static void initialize(Activity activity) {
        currentContext = activity;

        String dataDir = activity.getApplicationInfo().dataDir;
        String libPath = dataDir + "/lib.zip";
        // copy zipped python stdlib to data dir
        if(!(new File(libPath)).exists()) {
            System.out.println("copying stdlib");
            PyGlue.copyFile(activity.getAssets(), "lib.zip", libPath);
        }
        if(!(new File(dataDir + "/lib-dynload")).exists()) {
            System.out.println("extracting lib-dynload");
            PyGlue.extractFromZip(libPath, "lib-dynload", dataDir + "/");
        }
        // always copy app across
        PyGlue.copyFileOrDir(activity.getAssets(), "app", dataDir + "/app/");
        // initialize python bindings
        PyGlue.initWithHome(libPath, dataDir + "/lib-dynload/", dataDir + "/");
    }

    public static void copyFileOrDir(AssetManager assetManager, String path, String destPath) {
        String assets[];
        try {
            assets = assetManager.list(path);
            if (assets.length == 0) {
                copyFile(assetManager, path, destPath);
            } else {
                File dir = new File(destPath);
                if (!dir.exists())
                    dir.mkdir();
                for (int i = 0; i < assets.length; ++i)
                    copyFileOrDir(assetManager, path + "/" + assets[i], destPath + "/" + assets[i]);
            }
        } catch (IOException ex) {
            Log.e("tag", "I/O Exception", ex);
        }
    }

    public static void copyFile(AssetManager assetManager, String filename, String destFilename) {
        try {
            InputStream in = assetManager.open(filename);
            OutputStream out = new FileOutputStream(destFilename);

            int read;
            byte[] buffer = new byte[1024];
            while ((read = in.read(buffer)) != -1)
                out.write(buffer, 0, read);

            in.close();
            out.flush();
            out.close();
        } catch (Exception e) {
            Log.e("tag", e.getMessage());
        }
    }

    public static boolean unpackZipAsset(AssetManager assetManager, String zipPath, String destPath)
    {
        try {
            InputStream is = assetManager.open(zipPath);
            ZipInputStream zis = new ZipInputStream(new BufferedInputStream(is));

            ZipEntry zipEntry;
            while ((zipEntry = zis.getNextEntry()) != null)
            {
                String filename = zipEntry.getName();

                if(zipEntry.isDirectory()) {
                    File fmd = new File(destPath + filename);
                    fmd.mkdirs();
                    continue;
                }

                FileOutputStream fos = new FileOutputStream(destPath + filename);

                int count;
                byte[] buffer = new byte[1024];
                while((count = zis.read(buffer)) != -1)
                    fos.write(buffer, 0, count);

                fos.close();
                zis.closeEntry();
            }

            zis.close();
        }
        catch(IOException e) {
            e.printStackTrace();
            return false;
        }
        return  true;
    }

    public static boolean extractFromZip(String zipPath, String innerPath, String destPath)
    {
        while(innerPath.endsWith("/"))
            innerPath = innerPath.substring(0, innerPath.length() - 1);

        try {
            InputStream is = new FileInputStream(zipPath);
            ZipInputStream zis = new ZipInputStream(new BufferedInputStream(is));

            ZipEntry zipEntry;
            while((zipEntry = zis.getNextEntry()) != null)
            {
                String filename = zipEntry.getName();
                if(filename.startsWith(innerPath))
                {
                    if(zipEntry.isDirectory()) {
                        new File(destPath + filename).mkdirs();
                        zis.closeEntry();
                        continue;
                    }

                    FileOutputStream fos = new FileOutputStream(destPath + filename);

                    int count;
                    byte[] buffer = new byte[1024];
                    while((count = zis.read(buffer)) != -1)
                        fos.write(buffer, 0, count);

                    fos.close();
                }

                zis.closeEntry();
            }

            zis.close();
        } catch(IOException e) {
            // fall-through
        }
        return false;
    }
}
