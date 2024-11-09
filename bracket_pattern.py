from contextlib import contextmanager
import logging


logging.basicConfig(level = logging.INFO)


class ResourceActionError(Exception):
    def __init__(self):
        self.message = "Oops!"
        
class ResourceAcquisitionError(Exception):
    def __init__(self):
        self.message = "Failed to acquire resource!"


class Resource:
    def __init__(self, with_error = False):

        if with_error:

            raise ResourceAcquisitionError()
        
        return

    def doSomething(self):

        logging.info("Resource doing something!")
        logging.info("Performing some actions...")

    def doSomethingWithError(self):

        logging.error("Resource doing something that will throw an errors!")

        raise ResourceActionError()
    
    def release(self):

        logging.info("Releasing resource now.")
        
            
@contextmanager
def resourceManager(res: Resource):
    """Context manager for Resource
    
    Parameters
    ==========
    res : Resource
        Resource to be used
    """
    
    try:
        yield res

    except ResourceActionError as e:
        logging.error(e.message)
        
        logging.info("Handle errors.")
        
        logging.info("Performing error remediation actions...")
        
    finally:
        logging.info("Cleaning up!")
        
        logging.info("Performing custom clean up actions...")
        
        res.release()
        
        
def program(with_acquisition_error: bool = False, with_action_error: bool = False):
    """Demo program to simulate the various ways the bracket pattern will ensure resource closure.
    
    Parameters
    ==========
    with_acquisition_error : bool
        Simulates the case where resource fails to be acquired
    
    with_action_error : bool
        Simulates the case where the resource is acquired by an error is thrown when performing an action with the resource
    
    """
    
    try:
        
        logging.info("Acquiring resource...")
        
        resource = Resource(with_error=with_acquisition_error)
        
    except ResourceAcquisitionError as e:
        
        logging.error(e.message)
        
        logging.info("Performing acquisition failure remediation.... Maybe some form of retry...")
        
    else: 
        
        with resourceManager(resource) as res:
            
            if with_action_error:
                res.doSomethingWithError()
            else:
                res.doSomething()
            
    finally:
        
        logging.info("Ending program.")        

if __name__ == "__main__":
    
    print("#"*10 + " Normal program " + "#"*10)
    
    program()
    
    print("\n\n")
    
    print("#"*10 + " Normal program with action errors" + "#"*10)
    
    program(with_action_error=True)
    
    print("\n\n")
    
    print("#"*10 + " Program fails to acquire resource " + "#"*10)
    
    program(with_acquisition_error=True)