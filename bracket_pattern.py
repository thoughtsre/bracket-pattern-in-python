from contextlib import contextmanager
import logging


logging.basicConfig(level = logging.INFO)


class Resource:
    def __init__(self, with_error = False):

        if with_error:

            raise Exception("Failed to acquire resource!")
        
        return

    def doSomething(self):

        logging.info("Resource doing something!")

    def doSomethingWithError(self):

        logging.error("Doing something that will throw an errors!")

        raise Exception("Opps!")
    
    def release(self):

        logging.info("Releasing connction now.")

    

@contextmanager
def getResource(*args, **kwargs):

    try:
        res= Resource(*args, **kwargs)

        yield res

    except:
        logging.info("Handle errors.")
        
    finally:
        logging.info("Cleaning up!")
        
        res.release()


if __name__ == "__main__":

    with getResource() as resource:

        resource.doSomething()
        # resource.doSomethingWithError()