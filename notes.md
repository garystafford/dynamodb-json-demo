```bash
aws cloudformation create-stack \
    --stack-name dynamodb-product-stack \
    --template-body file://dynamodb-product.yml

python3 put_json_to_dynamo.py
```
