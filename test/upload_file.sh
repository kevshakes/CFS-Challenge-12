#!/bin/sh

aws s3 cp KEVIN-TUEI.jpg s3://my-company-personnel-storage-direct-clam/photos/portrait/ --metadata x-amz-meta-name=Kevin,x-amz-meta-surname=Tuei

