import logging, logging.config

try:

    logging.config.fileConfig("tachoproject/logs/log.ini")
    logger = logging.getLogger('appLogger')

except:

    log_file = "./logfile.log"
    log_level = logging.INFO
    logging.basicConfig(level=log_level, filename=log_file, filemode="w+",
                            format="%(asctime)-15s %(levelname)-8s %(message)s")
    logger = logging.getLogger()

def wrap(pre, post):
	""" Wrapper """
	def decorate(func):
		""" Decorator """
		def call(*args, **kwargs):
			""" Actual wrapping """
			pre(func)
			result = func(*args, **kwargs)
			post(func)
			return result
		return call
	return decorate

def entering(func, *args):
	""" Pre function logging """
	logger.debug("Entered %s", func.__name__)
	logger.info(func.__doc__)
	logger.info("Function at line %d in %s" %
		(func.__code__.co_firstlineno, func.__code__.co_filename))
	try:
		logger.warn("The argument %s is %s" % (func.__code__.co_varnames[0], *args))
	except IndexError:
		logger.warn("No arguments")

def exiting(func):
	""" Post function logging """
	logger.debug("Exited  %s", func.__name__)