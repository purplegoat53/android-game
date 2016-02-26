import ctypes
libgles2 = ctypes.cdll.LoadLibrary("libGLESv2.so")

GL_ES_VERSION_2_0 = 1
GL_DEPTH_BUFFER_BIT = 0x00000100
GL_STENCIL_BUFFER_BIT = 0x00000400
GL_COLOR_BUFFER_BIT = 0x00004000
GL_FALSE = 0
GL_TRUE = 1
GL_POINTS = 0x0000
GL_LINES = 0x0001
GL_LINE_LOOP = 0x0002
GL_LINE_STRIP = 0x0003
GL_TRIANGLES = 0x0004
GL_TRIANGLE_STRIP = 0x0005
GL_TRIANGLE_FAN = 0x0006
GL_ZERO = 0
GL_ONE = 1
GL_SRC_COLOR = 0x0300
GL_ONE_MINUS_SRC_COLOR = 0x0301
GL_SRC_ALPHA = 0x0302
GL_ONE_MINUS_SRC_ALPHA = 0x0303
GL_DST_ALPHA = 0x0304
GL_ONE_MINUS_DST_ALPHA = 0x0305
GL_DST_COLOR = 0x0306
GL_ONE_MINUS_DST_COLOR = 0x0307
GL_SRC_ALPHA_SATURATE = 0x0308
GL_FUNC_ADD = 0x8006
GL_BLEND_EQUATION = 0x8009
GL_BLEND_EQUATION_RGB = 0x8009
GL_BLEND_EQUATION_ALPHA = 0x883D
GL_FUNC_SUBTRACT = 0x800A
GL_FUNC_REVERSE_SUBTRACT = 0x800B
GL_BLEND_DST_RGB = 0x80C8
GL_BLEND_SRC_RGB = 0x80C9
GL_BLEND_DST_ALPHA = 0x80CA
GL_BLEND_SRC_ALPHA = 0x80CB
GL_CONSTANT_COLOR = 0x8001
GL_ONE_MINUS_CONSTANT_COLOR = 0x8002
GL_CONSTANT_ALPHA = 0x8003
GL_ONE_MINUS_CONSTANT_ALPHA = 0x8004
GL_BLEND_COLOR = 0x8005
GL_ARRAY_BUFFER = 0x8892
GL_ELEMENT_ARRAY_BUFFER = 0x8893
GL_ARRAY_BUFFER_BINDING = 0x8894
GL_ELEMENT_ARRAY_BUFFER_BINDING = 0x8895
GL_STREAM_DRAW = 0x88E0
GL_STATIC_DRAW = 0x88E4
GL_DYNAMIC_DRAW = 0x88E8
GL_BUFFER_SIZE = 0x8764
GL_BUFFER_USAGE = 0x8765
GL_CURRENT_VERTEX_ATTRIB = 0x8626
GL_FRONT = 0x0404
GL_BACK = 0x0405
GL_FRONT_AND_BACK = 0x0408
GL_TEXTURE_2D = 0x0DE1
GL_CULL_FACE = 0x0B44
GL_BLEND = 0x0BE2
GL_DITHER = 0x0BD0
GL_STENCIL_TEST = 0x0B90
GL_DEPTH_TEST = 0x0B71
GL_SCISSOR_TEST = 0x0C11
GL_POLYGON_OFFSET_FILL = 0x8037
GL_SAMPLE_ALPHA_TO_COVERAGE = 0x809E
GL_SAMPLE_COVERAGE = 0x80A0
GL_NO_ERROR = 0
GL_INVALID_ENUM = 0x0500
GL_INVALID_VALUE = 0x0501
GL_INVALID_OPERATION = 0x0502
GL_OUT_OF_MEMORY = 0x0505
GL_CW = 0x0900
GL_CCW = 0x0901
GL_LINE_WIDTH = 0x0B21
GL_ALIASED_POINT_SIZE_RANGE = 0x846D
GL_ALIASED_LINE_WIDTH_RANGE = 0x846E
GL_CULL_FACE_MODE = 0x0B45
GL_FRONT_FACE = 0x0B46
GL_DEPTH_RANGE = 0x0B70
GL_DEPTH_WRITEMASK = 0x0B72
GL_DEPTH_CLEAR_VALUE = 0x0B73
GL_DEPTH_FUNC = 0x0B74
GL_STENCIL_CLEAR_VALUE = 0x0B91
GL_STENCIL_FUNC = 0x0B92
GL_STENCIL_FAIL = 0x0B94
GL_STENCIL_PASS_DEPTH_FAIL = 0x0B95
GL_STENCIL_PASS_DEPTH_PASS = 0x0B96
GL_STENCIL_REF = 0x0B97
GL_STENCIL_VALUE_MASK = 0x0B93
GL_STENCIL_WRITEMASK = 0x0B98
GL_STENCIL_BACK_FUNC = 0x8800
GL_STENCIL_BACK_FAIL = 0x8801
GL_STENCIL_BACK_PASS_DEPTH_FAIL = 0x8802
GL_STENCIL_BACK_PASS_DEPTH_PASS = 0x8803
GL_STENCIL_BACK_REF = 0x8CA3
GL_STENCIL_BACK_VALUE_MASK = 0x8CA4
GL_STENCIL_BACK_WRITEMASK = 0x8CA5
GL_VIEWPORT = 0x0BA2
GL_SCISSOR_BOX = 0x0C10
GL_COLOR_CLEAR_VALUE = 0x0C22
GL_COLOR_WRITEMASK = 0x0C23
GL_UNPACK_ALIGNMENT = 0x0CF5
GL_PACK_ALIGNMENT = 0x0D05
GL_MAX_TEXTURE_SIZE = 0x0D33
GL_MAX_VIEWPORT_DIMS = 0x0D3A
GL_SUBPIXEL_BITS = 0x0D50
GL_RED_BITS = 0x0D52
GL_GREEN_BITS = 0x0D53
GL_BLUE_BITS = 0x0D54
GL_ALPHA_BITS = 0x0D55
GL_DEPTH_BITS = 0x0D56
GL_STENCIL_BITS = 0x0D57
GL_POLYGON_OFFSET_UNITS = 0x2A00
GL_POLYGON_OFFSET_FACTOR = 0x8038
GL_TEXTURE_BINDING_2D = 0x8069
GL_SAMPLE_BUFFERS = 0x80A8
GL_SAMPLES = 0x80A9
GL_SAMPLE_COVERAGE_VALUE = 0x80AA
GL_SAMPLE_COVERAGE_INVERT = 0x80AB
GL_NUM_COMPRESSED_TEXTURE_FORMATS = 0x86A2
GL_COMPRESSED_TEXTURE_FORMATS = 0x86A3
GL_DONT_CARE = 0x1100
GL_FASTEST = 0x1101
GL_NICEST = 0x1102
GL_GENERATE_MIPMAP_HINT = 0x8192
GL_BYTE = 0x1400
GL_UNSIGNED_BYTE = 0x1401
GL_SHORT = 0x1402
GL_UNSIGNED_SHORT = 0x1403
GL_INT = 0x1404
GL_UNSIGNED_INT = 0x1405
GL_FLOAT = 0x1406
GL_FIXED = 0x140C
GL_DEPTH_COMPONENT = 0x1902
GL_ALPHA = 0x1906
GL_RGB = 0x1907
GL_RGBA = 0x1908
GL_LUMINANCE = 0x1909
GL_LUMINANCE_ALPHA = 0x190A
GL_UNSIGNED_SHORT_4_4_4_4 = 0x8033
GL_UNSIGNED_SHORT_5_5_5_1 = 0x8034
GL_UNSIGNED_SHORT_5_6_5 = 0x8363
GL_FRAGMENT_SHADER = 0x8B30
GL_VERTEX_SHADER = 0x8B31
GL_MAX_VERTEX_ATTRIBS = 0x8869
GL_MAX_VERTEX_UNIFORM_VECTORS = 0x8DFB
GL_MAX_VARYING_VECTORS = 0x8DFC
GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS = 0x8B4D
GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS = 0x8B4C
GL_MAX_TEXTURE_IMAGE_UNITS = 0x8872
GL_MAX_FRAGMENT_UNIFORM_VECTORS = 0x8DFD
GL_SHADER_TYPE = 0x8B4F
GL_DELETE_STATUS = 0x8B80
GL_LINK_STATUS = 0x8B82
GL_VALIDATE_STATUS = 0x8B83
GL_ATTACHED_SHADERS = 0x8B85
GL_ACTIVE_UNIFORMS = 0x8B86
GL_ACTIVE_UNIFORM_MAX_LENGTH = 0x8B87
GL_ACTIVE_ATTRIBUTES = 0x8B89
GL_ACTIVE_ATTRIBUTE_MAX_LENGTH = 0x8B8A
GL_SHADING_LANGUAGE_VERSION = 0x8B8C
GL_CURRENT_PROGRAM = 0x8B8D
GL_NEVER = 0x0200
GL_LESS = 0x0201
GL_EQUAL = 0x0202
GL_LEQUAL = 0x0203
GL_GREATER = 0x0204
GL_NOTEQUAL = 0x0205
GL_GEQUAL = 0x0206
GL_ALWAYS = 0x0207
GL_KEEP = 0x1E00
GL_REPLACE = 0x1E01
GL_INCR = 0x1E02
GL_DECR = 0x1E03
GL_INVERT = 0x150A
GL_INCR_WRAP = 0x8507
GL_DECR_WRAP = 0x8508
GL_VENDOR = 0x1F00
GL_RENDERER = 0x1F01
GL_VERSION = 0x1F02
GL_EXTENSIONS = 0x1F03
GL_NEAREST = 0x2600
GL_LINEAR = 0x2601
GL_NEAREST_MIPMAP_NEAREST = 0x2700
GL_LINEAR_MIPMAP_NEAREST = 0x2701
GL_NEAREST_MIPMAP_LINEAR = 0x2702
GL_LINEAR_MIPMAP_LINEAR = 0x2703
GL_TEXTURE_MAG_FILTER = 0x2800
GL_TEXTURE_MIN_FILTER = 0x2801
GL_TEXTURE_WRAP_S = 0x2802
GL_TEXTURE_WRAP_T = 0x2803
GL_TEXTURE = 0x1702
GL_TEXTURE_CUBE_MAP = 0x8513
GL_TEXTURE_BINDING_CUBE_MAP = 0x8514
GL_TEXTURE_CUBE_MAP_POSITIVE_X = 0x8515
GL_TEXTURE_CUBE_MAP_NEGATIVE_X = 0x8516
GL_TEXTURE_CUBE_MAP_POSITIVE_Y = 0x8517
GL_TEXTURE_CUBE_MAP_NEGATIVE_Y = 0x8518
GL_TEXTURE_CUBE_MAP_POSITIVE_Z = 0x8519
GL_TEXTURE_CUBE_MAP_NEGATIVE_Z = 0x851A
GL_MAX_CUBE_MAP_TEXTURE_SIZE = 0x851C
GL_TEXTURE0 = 0x84C0
GL_TEXTURE1 = 0x84C1
GL_TEXTURE2 = 0x84C2
GL_TEXTURE3 = 0x84C3
GL_TEXTURE4 = 0x84C4
GL_TEXTURE5 = 0x84C5
GL_TEXTURE6 = 0x84C6
GL_TEXTURE7 = 0x84C7
GL_TEXTURE8 = 0x84C8
GL_TEXTURE9 = 0x84C9
GL_TEXTURE10 = 0x84CA
GL_TEXTURE11 = 0x84CB
GL_TEXTURE12 = 0x84CC
GL_TEXTURE13 = 0x84CD
GL_TEXTURE14 = 0x84CE
GL_TEXTURE15 = 0x84CF
GL_TEXTURE16 = 0x84D0
GL_TEXTURE17 = 0x84D1
GL_TEXTURE18 = 0x84D2
GL_TEXTURE19 = 0x84D3
GL_TEXTURE20 = 0x84D4
GL_TEXTURE21 = 0x84D5
GL_TEXTURE22 = 0x84D6
GL_TEXTURE23 = 0x84D7
GL_TEXTURE24 = 0x84D8
GL_TEXTURE25 = 0x84D9
GL_TEXTURE26 = 0x84DA
GL_TEXTURE27 = 0x84DB
GL_TEXTURE28 = 0x84DC
GL_TEXTURE29 = 0x84DD
GL_TEXTURE30 = 0x84DE
GL_TEXTURE31 = 0x84DF
GL_ACTIVE_TEXTURE = 0x84E0
GL_REPEAT = 0x2901
GL_CLAMP_TO_EDGE = 0x812F
GL_MIRRORED_REPEAT = 0x8370
GL_FLOAT_VEC2 = 0x8B50
GL_FLOAT_VEC3 = 0x8B51
GL_FLOAT_VEC4 = 0x8B52
GL_INT_VEC2 = 0x8B53
GL_INT_VEC3 = 0x8B54
GL_INT_VEC4 = 0x8B55
GL_BOOL = 0x8B56
GL_BOOL_VEC2 = 0x8B57
GL_BOOL_VEC3 = 0x8B58
GL_BOOL_VEC4 = 0x8B59
GL_FLOAT_MAT2 = 0x8B5A
GL_FLOAT_MAT3 = 0x8B5B
GL_FLOAT_MAT4 = 0x8B5C
GL_SAMPLER_2D = 0x8B5E
GL_SAMPLER_CUBE = 0x8B60
GL_VERTEX_ATTRIB_ARRAY_ENABLED = 0x8622
GL_VERTEX_ATTRIB_ARRAY_SIZE = 0x8623
GL_VERTEX_ATTRIB_ARRAY_STRIDE = 0x8624
GL_VERTEX_ATTRIB_ARRAY_TYPE = 0x8625
GL_VERTEX_ATTRIB_ARRAY_NORMALIZED = 0x886A
GL_VERTEX_ATTRIB_ARRAY_POINTER = 0x8645
GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING = 0x889F
GL_IMPLEMENTATION_COLOR_READ_TYPE = 0x8B9A
GL_IMPLEMENTATION_COLOR_READ_FORMAT = 0x8B9B
GL_COMPILE_STATUS = 0x8B81
GL_INFO_LOG_LENGTH = 0x8B84
GL_SHADER_SOURCE_LENGTH = 0x8B88
GL_SHADER_COMPILER = 0x8DFA
GL_SHADER_BINARY_FORMATS = 0x8DF8
GL_NUM_SHADER_BINARY_FORMATS = 0x8DF9
GL_LOW_FLOAT = 0x8DF0
GL_MEDIUM_FLOAT = 0x8DF1
GL_HIGH_FLOAT = 0x8DF2
GL_LOW_INT = 0x8DF3
GL_MEDIUM_INT = 0x8DF4
GL_HIGH_INT = 0x8DF5
GL_FRAMEBUFFER = 0x8D40
GL_RENDERBUFFER = 0x8D41
GL_RGBA4 = 0x8056
GL_RGB5_A1 = 0x8057
GL_RGB565 = 0x8D62
GL_DEPTH_COMPONENT16 = 0x81A5
GL_STENCIL_INDEX = 0x1901
GL_STENCIL_INDEX8 = 0x8D48
GL_RENDERBUFFER_WIDTH = 0x8D42
GL_RENDERBUFFER_HEIGHT = 0x8D43
GL_RENDERBUFFER_INTERNAL_FORMAT = 0x8D44
GL_RENDERBUFFER_RED_SIZE = 0x8D50
GL_RENDERBUFFER_GREEN_SIZE = 0x8D51
GL_RENDERBUFFER_BLUE_SIZE = 0x8D52
GL_RENDERBUFFER_ALPHA_SIZE = 0x8D53
GL_RENDERBUFFER_DEPTH_SIZE = 0x8D54
GL_RENDERBUFFER_STENCIL_SIZE = 0x8D55
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE = 0x8CD0
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME = 0x8CD1
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL = 0x8CD2
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE = 0x8CD3
GL_COLOR_ATTACHMENT0 = 0x8CE0
GL_DEPTH_ATTACHMENT = 0x8D00
GL_STENCIL_ATTACHMENT = 0x8D20
GL_NONE = 0
GL_FRAMEBUFFER_COMPLETE = 0x8CD5
GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT = 0x8CD6
GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT = 0x8CD7
GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS = 0x8CD9
GL_FRAMEBUFFER_UNSUPPORTED = 0x8CDD
GL_FRAMEBUFFER_BINDING = 0x8CA6
GL_RENDERBUFFER_BINDING = 0x8CA7
GL_MAX_RENDERBUFFER_SIZE = 0x84E8
GL_INVALID_FRAMEBUFFER_OPERATION = 0x0506

# GL_APICALL void         GL_APIENTRY glActiveTexture (GLenum texture);

glActiveTexture = libgles2.glActiveTexture
glActiveTexture.argtypes = [ctypes.c_uint]
glActiveTexture.restype = None

# GL_APICALL void         GL_APIENTRY glAttachShader (GLuint program, GLuint shader);

glAttachShader = libgles2.glAttachShader
glAttachShader.argtypes = [ctypes.c_uint, ctypes.c_uint]
glAttachShader.restype = None

# GL_APICALL void         GL_APIENTRY glBindAttribLocation (GLuint program, GLuint index, const GLchar* name);

glBindAttribLocation = libgles2.glBindAttribLocation
glBindAttribLocation.argtypes = [ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_char)]
glBindAttribLocation.restype = None

# GL_APICALL void         GL_APIENTRY glBindBuffer (GLenum target, GLuint buffer);

glBindBuffer = libgles2.glBindBuffer
glBindBuffer.argtypes = [ctypes.c_uint, ctypes.c_uint]
glBindBuffer.restype = None

# GL_APICALL void         GL_APIENTRY glBindFramebuffer (GLenum target, GLuint framebuffer);

glBindFramebuffer = libgles2.glBindFramebuffer
glBindFramebuffer.argtypes = [ctypes.c_uint, ctypes.c_uint]
glBindFramebuffer.restype = None

# GL_APICALL void         GL_APIENTRY glBindRenderbuffer (GLenum target, GLuint renderbuffer);

glBindRenderbuffer = libgles2.glBindRenderbuffer
glBindRenderbuffer.argtypes = [ctypes.c_uint, ctypes.c_uint]
glBindRenderbuffer.restype = None

# GL_APICALL void         GL_APIENTRY glBindTexture (GLenum target, GLuint texture);

glBindTexture = libgles2.glBindTexture
glBindTexture.argtypes = [ctypes.c_uint, ctypes.c_uint]
glBindTexture.restype = None

# GL_APICALL void         GL_APIENTRY glBlendColor (GLclampf red, GLclampf green, GLclampf blue, GLclampf alpha);

glBlendColor = libgles2.glBlendColor
glBlendColor.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float]
glBlendColor.restype = None

# GL_APICALL void         GL_APIENTRY glBlendEquation ( GLenum mode );

glBlendEquation = libgles2.glBlendEquation
glBlendEquation.argtypes = [ctypes.c_uint]
glBlendEquation.restype = None

# GL_APICALL void         GL_APIENTRY glBlendEquationSeparate (GLenum modeRGB, GLenum modeAlpha);

glBlendEquationSeparate = libgles2.glBlendEquationSeparate
glBlendEquationSeparate.argtypes = [ctypes.c_uint, ctypes.c_uint]
glBlendEquationSeparate.restype = None

# GL_APICALL void         GL_APIENTRY glBlendFunc (GLenum sfactor, GLenum dfactor);

glBlendFunc = libgles2.glBlendFunc
glBlendFunc.argtypes = [ctypes.c_uint, ctypes.c_uint]
glBlendFunc.restype = None

# GL_APICALL void         GL_APIENTRY glBlendFuncSeparate (GLenum srcRGB, GLenum dstRGB, GLenum srcAlpha, GLenum dstAlpha);

glBlendFuncSeparate = libgles2.glBlendFuncSeparate
glBlendFuncSeparate.argtypes = [ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint]
glBlendFuncSeparate.restype = None

# GL_APICALL void         GL_APIENTRY glBufferData (GLenum target, GLsizeiptr size, const GLvoid* data, GLenum usage);

glBufferData = libgles2.glBufferData
glBufferData.argtypes = [ctypes.c_uint, ctypes.c_ssize_t, ctypes.POINTER(None), ctypes.c_uint]
glBufferData.restype = None

# GL_APICALL void         GL_APIENTRY glBufferSubData (GLenum target, GLintptr offset, GLsizeiptr size, const GLvoid* data);

glBufferSubData = libgles2.glBufferSubData
glBufferSubData.argtypes = [ctypes.c_uint, ctypes.POINTER(ctypes.c_int), ctypes.c_ssize_t, ctypes.POINTER(None)]
glBufferSubData.restype = None

# GL_APICALL GLenum       GL_APIENTRY glCheckFramebufferStatus (GLenum target);

glCheckFramebufferStatus = libgles2.glCheckFramebufferStatus
glCheckFramebufferStatus.argtypes = [ctypes.c_uint]
glCheckFramebufferStatus.restype = ctypes.c_uint

# GL_APICALL void         GL_APIENTRY glClear (GLbitfield mask);

glClear = libgles2.glClear
glClear.argtypes = [ctypes.c_uint]
glClear.restype = None

# GL_APICALL void         GL_APIENTRY glClearColor (GLclampf red, GLclampf green, GLclampf blue, GLclampf alpha);

glClearColor = libgles2.glClearColor
glClearColor.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float]
glClearColor.restype = None

# GL_APICALL void         GL_APIENTRY glClearDepthf (GLclampf depth);

glClearDepthf = libgles2.glClearDepthf
glClearDepthf.argtypes = [ctypes.c_float]
glClearDepthf.restype = None

# GL_APICALL void         GL_APIENTRY glClearStencil (GLint s);

glClearStencil = libgles2.glClearStencil
glClearStencil.argtypes = [ctypes.c_int]
glClearStencil.restype = None

# GL_APICALL void         GL_APIENTRY glColorMask (GLboolean red, GLboolean green, GLboolean blue, GLboolean alpha);

glColorMask = libgles2.glColorMask
glColorMask.argtypes = [ctypes.c_ubyte, ctypes.c_ubyte, ctypes.c_ubyte, ctypes.c_ubyte]
glColorMask.restype = None

# GL_APICALL void         GL_APIENTRY glCompileShader (GLuint shader);

glCompileShader = libgles2.glCompileShader
glCompileShader.argtypes = [ctypes.c_uint]
glCompileShader.restype = None

# GL_APICALL void         GL_APIENTRY glCompressedTexImage2D (GLenum target, GLint level, GLenum internalformat, GLsizei width, GLsizei height, GLint border, GLsizei imageSize, const GLvoid* data);

glCompressedTexImage2D = libgles2.glCompressedTexImage2D
glCompressedTexImage2D.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.c_uint, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(None)]
glCompressedTexImage2D.restype = None

# GL_APICALL void         GL_APIENTRY glCompressedTexSubImage2D (GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLsizei imageSize, const GLvoid* data);

glCompressedTexSubImage2D = libgles2.glCompressedTexSubImage2D
glCompressedTexSubImage2D.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_uint, ctypes.c_int, ctypes.POINTER(None)]
glCompressedTexSubImage2D.restype = None

# GL_APICALL void         GL_APIENTRY glCopyTexImage2D (GLenum target, GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei height, GLint border);

glCopyTexImage2D = libgles2.glCopyTexImage2D
glCopyTexImage2D.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.c_uint, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
glCopyTexImage2D.restype = None

# GL_APICALL void         GL_APIENTRY glCopyTexSubImage2D (GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width, GLsizei height);

glCopyTexSubImage2D = libgles2.glCopyTexSubImage2D
glCopyTexSubImage2D.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
glCopyTexSubImage2D.restype = None

# GL_APICALL GLuint       GL_APIENTRY glCreateProgram (void);

glCreateProgram = libgles2.glCreateProgram
glCreateProgram.argtypes = []
glCreateProgram.restype = ctypes.c_uint

# GL_APICALL GLuint       GL_APIENTRY glCreateShader (GLenum type);

glCreateShader = libgles2.glCreateShader
glCreateShader.argtypes = [ctypes.c_uint]
glCreateShader.restype = ctypes.c_uint

# GL_APICALL void         GL_APIENTRY glCullFace (GLenum mode);

glCullFace = libgles2.glCullFace
glCullFace.argtypes = [ctypes.c_uint]
glCullFace.restype = None

# GL_APICALL void         GL_APIENTRY glDeleteBuffers (GLsizei n, const GLuint* buffers);

glDeleteBuffers = libgles2.glDeleteBuffers
glDeleteBuffers.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_uint)]
glDeleteBuffers.restype = None

# GL_APICALL void         GL_APIENTRY glDeleteFramebuffers (GLsizei n, const GLuint* framebuffers);

glDeleteFramebuffers = libgles2.glDeleteFramebuffers
glDeleteFramebuffers.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_uint)]
glDeleteFramebuffers.restype = None

# GL_APICALL void         GL_APIENTRY glDeleteProgram (GLuint program);

glDeleteProgram = libgles2.glDeleteProgram
glDeleteProgram.argtypes = [ctypes.c_uint]
glDeleteProgram.restype = None

# GL_APICALL void         GL_APIENTRY glDeleteRenderbuffers (GLsizei n, const GLuint* renderbuffers);

glDeleteRenderbuffers = libgles2.glDeleteRenderbuffers
glDeleteRenderbuffers.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_uint)]
glDeleteRenderbuffers.restype = None

# GL_APICALL void         GL_APIENTRY glDeleteShader (GLuint shader);

glDeleteShader = libgles2.glDeleteShader
glDeleteShader.argtypes = [ctypes.c_uint]
glDeleteShader.restype = None

# GL_APICALL void         GL_APIENTRY glDeleteTextures (GLsizei n, const GLuint* textures);

glDeleteTextures = libgles2.glDeleteTextures
glDeleteTextures.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_uint)]
glDeleteTextures.restype = None

# GL_APICALL void         GL_APIENTRY glDepthFunc (GLenum func);

glDepthFunc = libgles2.glDepthFunc
glDepthFunc.argtypes = [ctypes.c_uint]
glDepthFunc.restype = None

# GL_APICALL void         GL_APIENTRY glDepthMask (GLboolean flag);

glDepthMask = libgles2.glDepthMask
glDepthMask.argtypes = [ctypes.c_ubyte]
glDepthMask.restype = None

# GL_APICALL void         GL_APIENTRY glDepthRangef (GLclampf zNear, GLclampf zFar);

glDepthRangef = libgles2.glDepthRangef
glDepthRangef.argtypes = [ctypes.c_float, ctypes.c_float]
glDepthRangef.restype = None

# GL_APICALL void         GL_APIENTRY glDetachShader (GLuint program, GLuint shader);

glDetachShader = libgles2.glDetachShader
glDetachShader.argtypes = [ctypes.c_uint, ctypes.c_uint]
glDetachShader.restype = None

# GL_APICALL void         GL_APIENTRY glDisable (GLenum cap);

glDisable = libgles2.glDisable
glDisable.argtypes = [ctypes.c_uint]
glDisable.restype = None

# GL_APICALL void         GL_APIENTRY glDisableVertexAttribArray (GLuint index);

glDisableVertexAttribArray = libgles2.glDisableVertexAttribArray
glDisableVertexAttribArray.argtypes = [ctypes.c_uint]
glDisableVertexAttribArray.restype = None

# GL_APICALL void         GL_APIENTRY glDrawArrays (GLenum mode, GLint first, GLsizei count);

glDrawArrays = libgles2.glDrawArrays
glDrawArrays.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.c_int]
glDrawArrays.restype = None

# GL_APICALL void         GL_APIENTRY glDrawElements (GLenum mode, GLsizei count, GLenum type, const GLvoid* indices);

glDrawElements = libgles2.glDrawElements
glDrawElements.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.c_uint, ctypes.POINTER(None)]
glDrawElements.restype = None

# GL_APICALL void         GL_APIENTRY glEnable (GLenum cap);

glEnable = libgles2.glEnable
glEnable.argtypes = [ctypes.c_uint]
glEnable.restype = None

# GL_APICALL void         GL_APIENTRY glEnableVertexAttribArray (GLuint index);

glEnableVertexAttribArray = libgles2.glEnableVertexAttribArray
glEnableVertexAttribArray.argtypes = [ctypes.c_uint]
glEnableVertexAttribArray.restype = None

# GL_APICALL void         GL_APIENTRY glFinish (void);

glFinish = libgles2.glFinish
glFinish.argtypes = []
glFinish.restype = None

# GL_APICALL void         GL_APIENTRY glFlush (void);

glFlush = libgles2.glFlush
glFlush.argtypes = []
glFlush.restype = None

# GL_APICALL void         GL_APIENTRY glFramebufferRenderbuffer (GLenum target, GLenum attachment, GLenum renderbuffertarget, GLuint renderbuffer);

glFramebufferRenderbuffer = libgles2.glFramebufferRenderbuffer
glFramebufferRenderbuffer.argtypes = [ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint]
glFramebufferRenderbuffer.restype = None

# GL_APICALL void         GL_APIENTRY glFramebufferTexture2D (GLenum target, GLenum attachment, GLenum textarget, GLuint texture, GLint level);

glFramebufferTexture2D = libgles2.glFramebufferTexture2D
glFramebufferTexture2D.argtypes = [ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.c_int]
glFramebufferTexture2D.restype = None

# GL_APICALL void         GL_APIENTRY glFrontFace (GLenum mode);

glFrontFace = libgles2.glFrontFace
glFrontFace.argtypes = [ctypes.c_uint]
glFrontFace.restype = None

# GL_APICALL void         GL_APIENTRY glGenBuffers (GLsizei n, GLuint* buffers);

glGenBuffers = libgles2.glGenBuffers
glGenBuffers.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_uint)]
glGenBuffers.restype = None

# GL_APICALL void         GL_APIENTRY glGenerateMipmap (GLenum target);

glGenerateMipmap = libgles2.glGenerateMipmap
glGenerateMipmap.argtypes = [ctypes.c_uint]
glGenerateMipmap.restype = None

# GL_APICALL void         GL_APIENTRY glGenFramebuffers (GLsizei n, GLuint* framebuffers);

glGenFramebuffers = libgles2.glGenFramebuffers
glGenFramebuffers.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_uint)]
glGenFramebuffers.restype = None

# GL_APICALL void         GL_APIENTRY glGenRenderbuffers (GLsizei n, GLuint* renderbuffers);

glGenRenderbuffers = libgles2.glGenRenderbuffers
glGenRenderbuffers.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_uint)]
glGenRenderbuffers.restype = None

# GL_APICALL void         GL_APIENTRY glGenTextures (GLsizei n, GLuint* textures);

glGenTextures = libgles2.glGenTextures
glGenTextures.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_uint)]
glGenTextures.restype = None

# GL_APICALL void         GL_APIENTRY glGetActiveAttrib (GLuint program, GLuint index, GLsizei bufsize, GLsizei* length, GLint* size, GLenum* type, GLchar* name);

glGetActiveAttrib = libgles2.glGetActiveAttrib
glGetActiveAttrib.argtypes = [ctypes.c_uint, ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(ctypes.c_char)]
glGetActiveAttrib.restype = None

# GL_APICALL void         GL_APIENTRY glGetActiveUniform (GLuint program, GLuint index, GLsizei bufsize, GLsizei* length, GLint* size, GLenum* type, GLchar* name);

glGetActiveUniform = libgles2.glGetActiveUniform
glGetActiveUniform.argtypes = [ctypes.c_uint, ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_uint), ctypes.POINTER(ctypes.c_char)]
glGetActiveUniform.restype = None

# GL_APICALL void         GL_APIENTRY glGetAttachedShaders (GLuint program, GLsizei maxcount, GLsizei* count, GLuint* shaders);

glGetAttachedShaders = libgles2.glGetAttachedShaders
glGetAttachedShaders.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_uint)]
glGetAttachedShaders.restype = None

# GL_APICALL GLint        GL_APIENTRY glGetAttribLocation (GLuint program, const GLchar* name);

glGetAttribLocation = libgles2.glGetAttribLocation
glGetAttribLocation.argtypes = [ctypes.c_uint, ctypes.POINTER(ctypes.c_char)]
glGetAttribLocation.restype = ctypes.c_int

# GL_APICALL void         GL_APIENTRY glGetBooleanv (GLenum pname, GLboolean* params);

glGetBooleanv = libgles2.glGetBooleanv
glGetBooleanv.argtypes = [ctypes.c_uint, ctypes.POINTER(ctypes.c_ubyte)]
glGetBooleanv.restype = None

# GL_APICALL void         GL_APIENTRY glGetBufferParameteriv (GLenum target, GLenum pname, GLint* params);

glGetBufferParameteriv = libgles2.glGetBufferParameteriv
glGetBufferParameteriv.argtypes = [ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_int)]
glGetBufferParameteriv.restype = None

# GL_APICALL GLenum       GL_APIENTRY glGetError (void);

glGetError = libgles2.glGetError
glGetError.argtypes = []
glGetError.restype = ctypes.c_uint

# GL_APICALL void         GL_APIENTRY glGetFloatv (GLenum pname, GLfloat* params);

glGetFloatv = libgles2.glGetFloatv
glGetFloatv.argtypes = [ctypes.c_uint, ctypes.POINTER(ctypes.c_float)]
glGetFloatv.restype = None

# GL_APICALL void         GL_APIENTRY glGetFramebufferAttachmentParameteriv (GLenum target, GLenum attachment, GLenum pname, GLint* params);

glGetFramebufferAttachmentParameteriv = libgles2.glGetFramebufferAttachmentParameteriv
glGetFramebufferAttachmentParameteriv.argtypes = [ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_int)]
glGetFramebufferAttachmentParameteriv.restype = None

# GL_APICALL void         GL_APIENTRY glGetIntegerv (GLenum pname, GLint* params);

glGetIntegerv = libgles2.glGetIntegerv
glGetIntegerv.argtypes = [ctypes.c_uint, ctypes.POINTER(ctypes.c_int)]
glGetIntegerv.restype = None

# GL_APICALL void         GL_APIENTRY glGetProgramiv (GLuint program, GLenum pname, GLint* params);

glGetProgramiv = libgles2.glGetProgramiv
glGetProgramiv.argtypes = [ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_int)]
glGetProgramiv.restype = None

# GL_APICALL void         GL_APIENTRY glGetProgramInfoLog (GLuint program, GLsizei bufsize, GLsizei* length, GLchar* infolog);

glGetProgramInfoLog = libgles2.glGetProgramInfoLog
glGetProgramInfoLog.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_char)]
glGetProgramInfoLog.restype = None

# GL_APICALL void         GL_APIENTRY glGetRenderbufferParameteriv (GLenum target, GLenum pname, GLint* params);

glGetRenderbufferParameteriv = libgles2.glGetRenderbufferParameteriv
glGetRenderbufferParameteriv.argtypes = [ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_int)]
glGetRenderbufferParameteriv.restype = None

# GL_APICALL void         GL_APIENTRY glGetShaderiv (GLuint shader, GLenum pname, GLint* params);

glGetShaderiv = libgles2.glGetShaderiv
glGetShaderiv.argtypes = [ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_int)]
glGetShaderiv.restype = None

# GL_APICALL void         GL_APIENTRY glGetShaderInfoLog (GLuint shader, GLsizei bufsize, GLsizei* length, GLchar* infolog);

glGetShaderInfoLog = libgles2.glGetShaderInfoLog
glGetShaderInfoLog.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_char)]
glGetShaderInfoLog.restype = None

# GL_APICALL void         GL_APIENTRY glGetShaderPrecisionFormat (GLenum shadertype, GLenum precisiontype, GLint* range, GLint* precision);

glGetShaderPrecisionFormat = libgles2.glGetShaderPrecisionFormat
glGetShaderPrecisionFormat.argtypes = [ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
glGetShaderPrecisionFormat.restype = None

# GL_APICALL void         GL_APIENTRY glGetShaderSource (GLuint shader, GLsizei bufsize, GLsizei* length, GLchar* source);

glGetShaderSource = libgles2.glGetShaderSource
glGetShaderSource.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_char)]
glGetShaderSource.restype = None

# GL_APICALL const GLubyte* GL_APIENTRY glGetString (GLenum name);

glGetString = libgles2.glGetString
glGetString.argtypes = [ctypes.c_uint]
glGetString.restype = ctypes.POINTER(ctypes.c_ubyte)

# GL_APICALL void         GL_APIENTRY glGetTexParameterfv (GLenum target, GLenum pname, GLfloat* params);

glGetTexParameterfv = libgles2.glGetTexParameterfv
glGetTexParameterfv.argtypes = [ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_float)]
glGetTexParameterfv.restype = None

# GL_APICALL void         GL_APIENTRY glGetTexParameteriv (GLenum target, GLenum pname, GLint* params);

glGetTexParameteriv = libgles2.glGetTexParameteriv
glGetTexParameteriv.argtypes = [ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_int)]
glGetTexParameteriv.restype = None

# GL_APICALL void         GL_APIENTRY glGetUniformfv (GLuint program, GLint location, GLfloat* params);

glGetUniformfv = libgles2.glGetUniformfv
glGetUniformfv.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
glGetUniformfv.restype = None

# GL_APICALL void         GL_APIENTRY glGetUniformiv (GLuint program, GLint location, GLint* params);

glGetUniformiv = libgles2.glGetUniformiv
glGetUniformiv.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
glGetUniformiv.restype = None

# GL_APICALL GLint        GL_APIENTRY glGetUniformLocation (GLuint program, const GLchar* name);

glGetUniformLocation = libgles2.glGetUniformLocation
glGetUniformLocation.argtypes = [ctypes.c_uint, ctypes.POINTER(ctypes.c_char)]
glGetUniformLocation.restype = ctypes.c_int

# GL_APICALL void         GL_APIENTRY glGetVertexAttribfv (GLuint index, GLenum pname, GLfloat* params);

glGetVertexAttribfv = libgles2.glGetVertexAttribfv
glGetVertexAttribfv.argtypes = [ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_float)]
glGetVertexAttribfv.restype = None

# GL_APICALL void         GL_APIENTRY glGetVertexAttribiv (GLuint index, GLenum pname, GLint* params);

glGetVertexAttribiv = libgles2.glGetVertexAttribiv
glGetVertexAttribiv.argtypes = [ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_int)]
glGetVertexAttribiv.restype = None

# GL_APICALL void         GL_APIENTRY glGetVertexAttribPointerv (GLuint index, GLenum pname, GLvoid** pointer);

glGetVertexAttribPointerv = libgles2.glGetVertexAttribPointerv
glGetVertexAttribPointerv.argtypes = [ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.POINTER(None))]
glGetVertexAttribPointerv.restype = None

# GL_APICALL void         GL_APIENTRY glHint (GLenum target, GLenum mode);

glHint = libgles2.glHint
glHint.argtypes = [ctypes.c_uint, ctypes.c_uint]
glHint.restype = None

# GL_APICALL GLboolean    GL_APIENTRY glIsBuffer (GLuint buffer);

glIsBuffer = libgles2.glIsBuffer
glIsBuffer.argtypes = [ctypes.c_uint]
glIsBuffer.restype = ctypes.c_ubyte

# GL_APICALL GLboolean    GL_APIENTRY glIsEnabled (GLenum cap);

glIsEnabled = libgles2.glIsEnabled
glIsEnabled.argtypes = [ctypes.c_uint]
glIsEnabled.restype = ctypes.c_ubyte

# GL_APICALL GLboolean    GL_APIENTRY glIsFramebuffer (GLuint framebuffer);

glIsFramebuffer = libgles2.glIsFramebuffer
glIsFramebuffer.argtypes = [ctypes.c_uint]
glIsFramebuffer.restype = ctypes.c_ubyte

# GL_APICALL GLboolean    GL_APIENTRY glIsProgram (GLuint program);

glIsProgram = libgles2.glIsProgram
glIsProgram.argtypes = [ctypes.c_uint]
glIsProgram.restype = ctypes.c_ubyte

# GL_APICALL GLboolean    GL_APIENTRY glIsRenderbuffer (GLuint renderbuffer);

glIsRenderbuffer = libgles2.glIsRenderbuffer
glIsRenderbuffer.argtypes = [ctypes.c_uint]
glIsRenderbuffer.restype = ctypes.c_ubyte

# GL_APICALL GLboolean    GL_APIENTRY glIsShader (GLuint shader);

glIsShader = libgles2.glIsShader
glIsShader.argtypes = [ctypes.c_uint]
glIsShader.restype = ctypes.c_ubyte

# GL_APICALL GLboolean    GL_APIENTRY glIsTexture (GLuint texture);

glIsTexture = libgles2.glIsTexture
glIsTexture.argtypes = [ctypes.c_uint]
glIsTexture.restype = ctypes.c_ubyte

# GL_APICALL void         GL_APIENTRY glLineWidth (GLfloat width);

glLineWidth = libgles2.glLineWidth
glLineWidth.argtypes = [ctypes.c_float]
glLineWidth.restype = None

# GL_APICALL void         GL_APIENTRY glLinkProgram (GLuint program);

glLinkProgram = libgles2.glLinkProgram
glLinkProgram.argtypes = [ctypes.c_uint]
glLinkProgram.restype = None

# GL_APICALL void         GL_APIENTRY glPixelStorei (GLenum pname, GLint param);

glPixelStorei = libgles2.glPixelStorei
glPixelStorei.argtypes = [ctypes.c_uint, ctypes.c_int]
glPixelStorei.restype = None

# GL_APICALL void         GL_APIENTRY glPolygonOffset (GLfloat factor, GLfloat units);

glPolygonOffset = libgles2.glPolygonOffset
glPolygonOffset.argtypes = [ctypes.c_float, ctypes.c_float]
glPolygonOffset.restype = None

# GL_APICALL void         GL_APIENTRY glReadPixels (GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type, GLvoid* pixels);

glReadPixels = libgles2.glReadPixels
glReadPixels.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(None)]
glReadPixels.restype = None

# GL_APICALL void         GL_APIENTRY glReleaseShaderCompiler (void);

glReleaseShaderCompiler = libgles2.glReleaseShaderCompiler
glReleaseShaderCompiler.argtypes = []
glReleaseShaderCompiler.restype = None

# GL_APICALL void         GL_APIENTRY glRenderbufferStorage (GLenum target, GLenum internalformat, GLsizei width, GLsizei height);

glRenderbufferStorage = libgles2.glRenderbufferStorage
glRenderbufferStorage.argtypes = [ctypes.c_uint, ctypes.c_uint, ctypes.c_int, ctypes.c_int]
glRenderbufferStorage.restype = None

# GL_APICALL void         GL_APIENTRY glSampleCoverage (GLclampf value, GLboolean invert);

glSampleCoverage = libgles2.glSampleCoverage
glSampleCoverage.argtypes = [ctypes.c_float, ctypes.c_ubyte]
glSampleCoverage.restype = None

# GL_APICALL void         GL_APIENTRY glScissor (GLint x, GLint y, GLsizei width, GLsizei height);

glScissor = libgles2.glScissor
glScissor.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
glScissor.restype = None

# GL_APICALL void         GL_APIENTRY glShaderBinary (GLsizei n, const GLuint* shaders, GLenum binaryformat, const GLvoid* binary, GLsizei length);

glShaderBinary = libgles2.glShaderBinary
glShaderBinary.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_uint), ctypes.c_uint, ctypes.POINTER(None), ctypes.c_int]
glShaderBinary.restype = None

# GL_APICALL void         GL_APIENTRY glShaderSource (GLuint shader, GLsizei count, const GLchar** string, const GLint* length);

glShaderSource = libgles2.glShaderSource
glShaderSource.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.POINTER(ctypes.c_char)), ctypes.POINTER(ctypes.c_int)]
glShaderSource.restype = None

# GL_APICALL void         GL_APIENTRY glStencilFunc (GLenum func, GLint ref, GLuint mask);

glStencilFunc = libgles2.glStencilFunc
glStencilFunc.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.c_uint]
glStencilFunc.restype = None

# GL_APICALL void         GL_APIENTRY glStencilFuncSeparate (GLenum face, GLenum func, GLint ref, GLuint mask);

glStencilFuncSeparate = libgles2.glStencilFuncSeparate
glStencilFuncSeparate.argtypes = [ctypes.c_uint, ctypes.c_uint, ctypes.c_int, ctypes.c_uint]
glStencilFuncSeparate.restype = None

# GL_APICALL void         GL_APIENTRY glStencilMask (GLuint mask);

glStencilMask = libgles2.glStencilMask
glStencilMask.argtypes = [ctypes.c_uint]
glStencilMask.restype = None

# GL_APICALL void         GL_APIENTRY glStencilMaskSeparate (GLenum face, GLuint mask);

glStencilMaskSeparate = libgles2.glStencilMaskSeparate
glStencilMaskSeparate.argtypes = [ctypes.c_uint, ctypes.c_uint]
glStencilMaskSeparate.restype = None

# GL_APICALL void         GL_APIENTRY glStencilOp (GLenum fail, GLenum zfail, GLenum zpass);

glStencilOp = libgles2.glStencilOp
glStencilOp.argtypes = [ctypes.c_uint, ctypes.c_uint, ctypes.c_uint]
glStencilOp.restype = None

# GL_APICALL void         GL_APIENTRY glStencilOpSeparate (GLenum face, GLenum fail, GLenum zfail, GLenum zpass);

glStencilOpSeparate = libgles2.glStencilOpSeparate
glStencilOpSeparate.argtypes = [ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint]
glStencilOpSeparate.restype = None

# GL_APICALL void         GL_APIENTRY glTexImage2D (GLenum target, GLint level, GLint internalformat, GLsizei width, GLsizei height, GLint border, GLenum format, GLenum type, const GLvoid* pixels);

glTexImage2D = libgles2.glTexImage2D
glTexImage2D.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(None)]
glTexImage2D.restype = None

# GL_APICALL void         GL_APIENTRY glTexParameterf (GLenum target, GLenum pname, GLfloat param);

glTexParameterf = libgles2.glTexParameterf
glTexParameterf.argtypes = [ctypes.c_uint, ctypes.c_uint, ctypes.c_float]
glTexParameterf.restype = None

# GL_APICALL void         GL_APIENTRY glTexParameterfv (GLenum target, GLenum pname, const GLfloat* params);

glTexParameterfv = libgles2.glTexParameterfv
glTexParameterfv.argtypes = [ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_float)]
glTexParameterfv.restype = None

# GL_APICALL void         GL_APIENTRY glTexParameteri (GLenum target, GLenum pname, GLint param);

glTexParameteri = libgles2.glTexParameteri
glTexParameteri.argtypes = [ctypes.c_uint, ctypes.c_uint, ctypes.c_int]
glTexParameteri.restype = None

# GL_APICALL void         GL_APIENTRY glTexParameteriv (GLenum target, GLenum pname, const GLint* params);

glTexParameteriv = libgles2.glTexParameteriv
glTexParameteriv.argtypes = [ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(ctypes.c_int)]
glTexParameteriv.restype = None

# GL_APICALL void         GL_APIENTRY glTexSubImage2D (GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const GLvoid* pixels);

glTexSubImage2D = libgles2.glTexSubImage2D
glTexSubImage2D.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_uint, ctypes.c_uint, ctypes.POINTER(None)]
glTexSubImage2D.restype = None

# GL_APICALL void         GL_APIENTRY glUniform1f (GLint location, GLfloat x);

glUniform1f = libgles2.glUniform1f
glUniform1f.argtypes = [ctypes.c_int, ctypes.c_float]
glUniform1f.restype = None

# GL_APICALL void         GL_APIENTRY glUniform1fv (GLint location, GLsizei count, const GLfloat* v);

glUniform1fv = libgles2.glUniform1fv
glUniform1fv.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
glUniform1fv.restype = None

# GL_APICALL void         GL_APIENTRY glUniform1i (GLint location, GLint x);

glUniform1i = libgles2.glUniform1i
glUniform1i.argtypes = [ctypes.c_int, ctypes.c_int]
glUniform1i.restype = None

# GL_APICALL void         GL_APIENTRY glUniform1iv (GLint location, GLsizei count, const GLint* v);

glUniform1iv = libgles2.glUniform1iv
glUniform1iv.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
glUniform1iv.restype = None

# GL_APICALL void         GL_APIENTRY glUniform2f (GLint location, GLfloat x, GLfloat y);

glUniform2f = libgles2.glUniform2f
glUniform2f.argtypes = [ctypes.c_int, ctypes.c_float, ctypes.c_float]
glUniform2f.restype = None

# GL_APICALL void         GL_APIENTRY glUniform2fv (GLint location, GLsizei count, const GLfloat* v);

glUniform2fv = libgles2.glUniform2fv
glUniform2fv.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
glUniform2fv.restype = None

# GL_APICALL void         GL_APIENTRY glUniform2i (GLint location, GLint x, GLint y);

glUniform2i = libgles2.glUniform2i
glUniform2i.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]
glUniform2i.restype = None

# GL_APICALL void         GL_APIENTRY glUniform2iv (GLint location, GLsizei count, const GLint* v);

glUniform2iv = libgles2.glUniform2iv
glUniform2iv.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
glUniform2iv.restype = None

# GL_APICALL void         GL_APIENTRY glUniform3f (GLint location, GLfloat x, GLfloat y, GLfloat z);

glUniform3f = libgles2.glUniform3f
glUniform3f.argtypes = [ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_float]
glUniform3f.restype = None

# GL_APICALL void         GL_APIENTRY glUniform3fv (GLint location, GLsizei count, const GLfloat* v);

glUniform3fv = libgles2.glUniform3fv
glUniform3fv.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
glUniform3fv.restype = None

# GL_APICALL void         GL_APIENTRY glUniform3i (GLint location, GLint x, GLint y, GLint z);

glUniform3i = libgles2.glUniform3i
glUniform3i.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
glUniform3i.restype = None

# GL_APICALL void         GL_APIENTRY glUniform3iv (GLint location, GLsizei count, const GLint* v);

glUniform3iv = libgles2.glUniform3iv
glUniform3iv.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
glUniform3iv.restype = None

# GL_APICALL void         GL_APIENTRY glUniform4f (GLint location, GLfloat x, GLfloat y, GLfloat z, GLfloat w);

glUniform4f = libgles2.glUniform4f
glUniform4f.argtypes = [ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float]
glUniform4f.restype = None

# GL_APICALL void         GL_APIENTRY glUniform4fv (GLint location, GLsizei count, const GLfloat* v);

glUniform4fv = libgles2.glUniform4fv
glUniform4fv.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
glUniform4fv.restype = None

# GL_APICALL void         GL_APIENTRY glUniform4i (GLint location, GLint x, GLint y, GLint z, GLint w);

glUniform4i = libgles2.glUniform4i
glUniform4i.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
glUniform4i.restype = None

# GL_APICALL void         GL_APIENTRY glUniform4iv (GLint location, GLsizei count, const GLint* v);

glUniform4iv = libgles2.glUniform4iv
glUniform4iv.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
glUniform4iv.restype = None

# GL_APICALL void         GL_APIENTRY glUniformMatrix2fv (GLint location, GLsizei count, GLboolean transpose, const GLfloat* value);

glUniformMatrix2fv = libgles2.glUniformMatrix2fv
glUniformMatrix2fv.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_ubyte, ctypes.POINTER(ctypes.c_float)]
glUniformMatrix2fv.restype = None

# GL_APICALL void         GL_APIENTRY glUniformMatrix3fv (GLint location, GLsizei count, GLboolean transpose, const GLfloat* value);

glUniformMatrix3fv = libgles2.glUniformMatrix3fv
glUniformMatrix3fv.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_ubyte, ctypes.POINTER(ctypes.c_float)]
glUniformMatrix3fv.restype = None

# GL_APICALL void         GL_APIENTRY glUniformMatrix4fv (GLint location, GLsizei count, GLboolean transpose, const GLfloat* value);

glUniformMatrix4fv = libgles2.glUniformMatrix4fv
glUniformMatrix4fv.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_ubyte, ctypes.POINTER(ctypes.c_float)]
glUniformMatrix4fv.restype = None

# GL_APICALL void         GL_APIENTRY glUseProgram (GLuint program);

glUseProgram = libgles2.glUseProgram
glUseProgram.argtypes = [ctypes.c_uint]
glUseProgram.restype = None

# GL_APICALL void         GL_APIENTRY glValidateProgram (GLuint program);

glValidateProgram = libgles2.glValidateProgram
glValidateProgram.argtypes = [ctypes.c_uint]
glValidateProgram.restype = None

# GL_APICALL void         GL_APIENTRY glVertexAttrib1f (GLuint indx, GLfloat x);

glVertexAttrib1f = libgles2.glVertexAttrib1f
glVertexAttrib1f.argtypes = [ctypes.c_uint, ctypes.c_float]
glVertexAttrib1f.restype = None

# GL_APICALL void         GL_APIENTRY glVertexAttrib1fv (GLuint indx, const GLfloat* values);

glVertexAttrib1fv = libgles2.glVertexAttrib1fv
glVertexAttrib1fv.argtypes = [ctypes.c_uint, ctypes.POINTER(ctypes.c_float)]
glVertexAttrib1fv.restype = None

# GL_APICALL void         GL_APIENTRY glVertexAttrib2f (GLuint indx, GLfloat x, GLfloat y);

glVertexAttrib2f = libgles2.glVertexAttrib2f
glVertexAttrib2f.argtypes = [ctypes.c_uint, ctypes.c_float, ctypes.c_float]
glVertexAttrib2f.restype = None

# GL_APICALL void         GL_APIENTRY glVertexAttrib2fv (GLuint indx, const GLfloat* values);

glVertexAttrib2fv = libgles2.glVertexAttrib2fv
glVertexAttrib2fv.argtypes = [ctypes.c_uint, ctypes.POINTER(ctypes.c_float)]
glVertexAttrib2fv.restype = None

# GL_APICALL void         GL_APIENTRY glVertexAttrib3f (GLuint indx, GLfloat x, GLfloat y, GLfloat z);

glVertexAttrib3f = libgles2.glVertexAttrib3f
glVertexAttrib3f.argtypes = [ctypes.c_uint, ctypes.c_float, ctypes.c_float, ctypes.c_float]
glVertexAttrib3f.restype = None

# GL_APICALL void         GL_APIENTRY glVertexAttrib3fv (GLuint indx, const GLfloat* values);

glVertexAttrib3fv = libgles2.glVertexAttrib3fv
glVertexAttrib3fv.argtypes = [ctypes.c_uint, ctypes.POINTER(ctypes.c_float)]
glVertexAttrib3fv.restype = None

# GL_APICALL void         GL_APIENTRY glVertexAttrib4f (GLuint indx, GLfloat x, GLfloat y, GLfloat z, GLfloat w);

glVertexAttrib4f = libgles2.glVertexAttrib4f
glVertexAttrib4f.argtypes = [ctypes.c_uint, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float]
glVertexAttrib4f.restype = None

# GL_APICALL void         GL_APIENTRY glVertexAttrib4fv (GLuint indx, const GLfloat* values);

glVertexAttrib4fv = libgles2.glVertexAttrib4fv
glVertexAttrib4fv.argtypes = [ctypes.c_uint, ctypes.POINTER(ctypes.c_float)]
glVertexAttrib4fv.restype = None

# GL_APICALL void         GL_APIENTRY glVertexAttribPointer (GLuint indx, GLint size, GLenum type, GLboolean normalized, GLsizei stride, const GLvoid* ptr);

glVertexAttribPointer = libgles2.glVertexAttribPointer
glVertexAttribPointer.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.c_uint, ctypes.c_ubyte, ctypes.c_int, ctypes.POINTER(None)]
glVertexAttribPointer.restype = None

# GL_APICALL void         GL_APIENTRY glViewport (GLint x, GLint y, GLsizei width, GLsizei height);

glViewport = libgles2.glViewport
glViewport.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
glViewport.restype = None
