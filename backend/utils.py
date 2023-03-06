from fastapi import status


class Response:
    def __init__(
        self, success=True, status_code=status.HTTP_200_OK, detail=None
    ) -> None:
        self.success = success
        self.status_code = status_code
        self.detail = detail
