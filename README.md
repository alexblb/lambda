Am creat fisierul lambdastack.yml care ar trebui sa imi creeze resursele:
    S3 bucket
    Lambda function
    
Am creat un rol pentru functia lambda prin care sa aibe full acces la s3 buckets

Urmand sa rulez urmatoarele comenzi:

aws cloudformation create-stack --stack-name awslambdastack --template-body file://lambdastack.yml

aws update-function-code --function-name lambdafun --zip-file code.zip

