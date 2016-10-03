from functools import wraps


def dump_func_name(logger, level='info'):
    """
    http://stackoverflow.com/questions/5929107/python-decorators-with-parameters
    """
    def func_name(func):
        @wraps(func)
        def echo_func(*func_args, **func_kwargs):
            # TODO: if, elif, else 대신에 Violent Python에서 좀 더 효율적인 방법을 제시했던것 같은데
            if level == 'info':
                logger.info('Start func: {}'.format(func.__name__))
            elif level == 'debug':
                logger.debug('Start func: {}'.format(func.__name__))
            else:
                ValueError('Check logger level: {}'.format(level))
            return func(*func_args, **func_kwargs)
        return echo_func
    return func_name