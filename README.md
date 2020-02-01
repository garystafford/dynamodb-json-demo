```bash
# create stack
aws cloudformation create-stack \
    --stack-name dynamodb-product-stack \
    --template-body file://dynamodb-product.yml

# write products to table
python3 put_json_to_dynamo.py

# scan table (read all)
aws dynamodb scan --table-name Products

# delete stack
aws cloudformation delete-stack \
    --stack-name dynamodb-product-stack
```
