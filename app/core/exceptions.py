class EVOSException(Exception):
    def __init__(self, message: str, code: str = "evos_error"):
        self.message = message
        self.code = code


class DatasetValidationError(EVOSException):
    def __init__(self, message: str):
        super().__init__(message, code="dataset_validation_error")


class SchedulingError(EVOSException):
    def __init__(self, message: str):
        super().__init__(message, code="scheduling_error")
