# Stubs for logging (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

CRITICAL = ...  # type: Any
FATAL = ...  # type: Any
ERROR = ...  # type: Any
WARNING = ...  # type: Any
WARN = ...  # type: Any
INFO = ...  # type: Any
DEBUG = ...  # type: Any
NOTSET = ...  # type: Any

def getLevelName(level): ...
def addLevelName(level, levelName): ...

class LogRecord:
    name = ...  # type: Any
    msg = ...  # type: Any
    args = ...  # type: Any
    levelname = ...  # type: Any
    levelno = ...  # type: Any
    pathname = ...  # type: Any
    filename = ...  # type: Any
    module = ...  # type: Any
    exc_info = ...  # type: Any
    exc_text = ...  # type: Any
    stack_info = ...  # type: Any
    lineno = ...  # type: Any
    funcName = ...  # type: Any
    created = ...  # type: Any
    msecs = ...  # type: Any
    relativeCreated = ...  # type: Any
    thread = ...  # type: Any
    threadName = ...  # type: Any
    processName = ...  # type: Any
    process = ...  # type: Any
    def __init__(self, name, level, pathname, lineno, msg, args, exc_info, func=None, sinfo=None,
                 **kwargs): ...
    def getMessage(self): ...

def setLogRecordFactory(factory): ...
def getLogRecordFactory(): ...
def makeLogRecord(dict): ...

class PercentStyle:
    default_format = ...  # type: Any
    asctime_format = ...  # type: Any
    asctime_search = ...  # type: Any
    def __init__(self, fmt): ...
    def usesTime(self): ...
    def format(self, record): ...

class StrFormatStyle(PercentStyle):
    default_format = ...  # type: Any
    asctime_format = ...  # type: Any
    asctime_search = ...  # type: Any
    def format(self, record): ...

class StringTemplateStyle(PercentStyle):
    default_format = ...  # type: Any
    asctime_format = ...  # type: Any
    asctime_search = ...  # type: Any
    def __init__(self, fmt): ...
    def usesTime(self): ...
    def format(self, record): ...

BASIC_FORMAT = ...  # type: Any

class Formatter:
    converter = ...  # type: Any
    datefmt = ...  # type: Any
    def __init__(self, fmt=None, datefmt=None, style=''): ...
    default_time_format = ...  # type: Any
    default_msec_format = ...  # type: Any
    def formatTime(self, record, datefmt=None): ...
    def formatException(self, ei): ...
    def usesTime(self): ...
    def formatMessage(self, record): ...
    def formatStack(self, stack_info): ...
    def format(self, record): ...

class BufferingFormatter:
    linefmt = ...  # type: Any
    def __init__(self, linefmt=None): ...
    def formatHeader(self, records): ...
    def formatFooter(self, records): ...
    def format(self, records): ...

class Filter:
    name = ...  # type: Any
    nlen = ...  # type: Any
    def __init__(self, name=''): ...
    def filter(self, record): ...

class Filterer:
    filters = ...  # type: Any
    def __init__(self): ...
    def addFilter(self, filter): ...
    def removeFilter(self, filter): ...
    def filter(self, record): ...

class Handler(Filterer):
    level = ...  # type: Any
    formatter = ...  # type: Any
    def __init__(self, level=...): ...
    def get_name(self): ...
    def set_name(self, name): ...
    name = ...  # type: Any
    lock = ...  # type: Any
    def createLock(self): ...
    def acquire(self): ...
    def release(self): ...
    def setLevel(self, level): ...
    def format(self, record): ...
    def emit(self, record): ...
    def handle(self, record): ...
    def setFormatter(self, fmt): ...
    def flush(self): ...
    def close(self): ...
    def handleError(self, record): ...

class StreamHandler(Handler):
    terminator = ...  # type: Any
    stream = ...  # type: Any
    def __init__(self, stream=None): ...
    def flush(self): ...
    def emit(self, record): ...

class FileHandler(StreamHandler):
    baseFilename = ...  # type: Any
    mode = ...  # type: Any
    encoding = ...  # type: Any
    delay = ...  # type: Any
    stream = ...  # type: Any
    def __init__(self, filename, mode='', encoding=None, delay=False): ...
    def close(self): ...
    def emit(self, record): ...

class _StderrHandler(StreamHandler):
    def __init__(self, level=...): ...

lastResort = ...  # type: Any

class PlaceHolder:
    loggerMap = ...  # type: Any
    def __init__(self, alogger): ...
    def append(self, alogger): ...

def setLoggerClass(klass): ...
def getLoggerClass(): ...

class Manager:
    root = ...  # type: Any
    disable = ...  # type: Any
    emittedNoHandlerWarning = ...  # type: Any
    loggerDict = ...  # type: Any
    loggerClass = ...  # type: Any
    logRecordFactory = ...  # type: Any
    def __init__(self, rootnode): ...
    def getLogger(self, name): ...
    def setLoggerClass(self, klass): ...
    def setLogRecordFactory(self, factory): ...

class Logger(Filterer):
    name = ...  # type: Any
    level = ...  # type: Any
    parent = ...  # type: Any
    propagate = ...  # type: Any
    handlers = ...  # type: Any
    disabled = ...  # type: Any
    def __init__(self, name, level=...): ...
    def setLevel(self, level): ...
    def debug(self, msg, *args, **kwargs): ...
    def info(self, msg, *args, **kwargs): ...
    def warning(self, msg, *args, **kwargs): ...
    def warn(self, msg, *args, **kwargs): ...
    def error(self, msg, *args, **kwargs): ...
    def exception(self, msg, *args, **kwargs): ...
    def critical(self, msg, *args, **kwargs): ...
    fatal = ...  # type: Any
    def log(self, level, msg, *args, **kwargs): ...
    def findCaller(self, stack_info=False): ...
    def makeRecord(self, name, level, fn, lno, msg, args, exc_info, func=None, extra=None,
                   sinfo=None): ...
    def handle(self, record): ...
    def addHandler(self, hdlr): ...
    def removeHandler(self, hdlr): ...
    def hasHandlers(self): ...
    def callHandlers(self, record): ...
    def getEffectiveLevel(self): ...
    def isEnabledFor(self, level): ...
    def getChild(self, suffix): ...

class RootLogger(Logger):
    def __init__(self, level): ...

class LoggerAdapter:
    logger = ...  # type: Any
    extra = ...  # type: Any
    def __init__(self, logger, extra): ...
    def process(self, msg, kwargs): ...
    def debug(self, msg, *args, **kwargs): ...
    def info(self, msg, *args, **kwargs): ...
    def warning(self, msg, *args, **kwargs): ...
    def warn(self, msg, *args, **kwargs): ...
    def error(self, msg, *args, **kwargs): ...
    def exception(self, msg, *args, **kwargs): ...
    def critical(self, msg, *args, **kwargs): ...
    def log(self, level, msg, *args, **kwargs): ...
    def isEnabledFor(self, level): ...
    def setLevel(self, level): ...
    def getEffectiveLevel(self): ...
    def hasHandlers(self): ...

def basicConfig(**kwargs): ...
def getLogger(name=None): ...
def critical(msg, *args, **kwargs): ...

fatal = ...  # type: Any

def error(msg, *args, **kwargs): ...
def exception(msg, *args, **kwargs): ...
def warning(msg, *args, **kwargs): ...
def warn(msg, *args, **kwargs): ...
def info(msg, *args, **kwargs): ...
def debug(msg, *args, **kwargs): ...
def log(level, msg, *args, **kwargs): ...
def disable(level): ...

class NullHandler(Handler):
    def handle(self, record): ...
    def emit(self, record): ...
    lock = ...  # type: Any
    def createLock(self): ...

def captureWarnings(capture): ...