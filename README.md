# Import JSON File to DynamoDB

## Commands
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

## References
- <https://github.com/GoogleCloudPlatform/microservices-demo>
- <https://github.com/GoogleCloudPlatform/microservices-demo/blob/master/src/productcatalogservice/products.json>
- <https://github.com/blueCycle>
- <http://a9b80aacd3e7011ea9e5b02173f1f8f2-1644737622.us-east-2.elb.amazonaws.com/cart>