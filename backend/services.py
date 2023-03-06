# std
import os
import concurrent.futures
from uuid import uuid4

# 3rd
import boto3
from loguru import logger
from fastapi import UploadFile, HTTPException, status
from dotenv import load_dotenv

load_dotenv()

# NOTE: Ключ выдуманный
AWS_SECRET_KEY = os.environ.get("AWS_SECRET_KEY")

S3 = boto3.resource("s3")
BUCKET = S3.Bucket(AWS_SECRET_KEY)


def s3_upload(file: UploadFile) -> None:
    """
    Upload to S3 Bucket
    """

    # NOTE: Имитация отправки файлов
    uuid_part = uuid4()
    # BUCKET.put_object(Key=f"{uuid_part}_{file.filename}", Body=file)

    logger.info(f"File {uuid_part}_{file.filename} uploded!")


def upload_files(files: list[UploadFile]) -> bool | HTTPException:
    """
    Multithreaded file upload
    """

    try:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = [executor.submit(s3_upload, file) for file in files]
    except:
        raise HTTPException(
            status_code=status.HTTP_200_OK,
            detail="The service is temporarily unavailable. Try again later!",
        )
    return True


def validate_files(files: list[UploadFile]) -> bool | HTTPException:
    """
    Validating of files existence
    """
    for file in files:
        if not file.filename:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Upload at least 1 file",
            )
    return True
