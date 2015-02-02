hosting_url = YOUR_DEPLOY_URL

success = hosting_url + '/success'

policy_document = {"expiration": "2016-01-01T00:00:00Z",
        "conditions": [
            {"bucket": "your_bucket"},
            ["starts-with", "$key", "uploads/"],
            {"acl": "private"},
            {"user": "converter"},
            {"success_action_redirect": success},
            ["content-length-range", 1, 1000048576]
            ]
        }

encoding_api_user_id = YOUR_ENCODING_API_USER
encoding_api_key = YOUR_ENCODING_API_KEY
encoding_url = "http://manage.encoding.com:80"

s3_key = YOUR_S3_KEY
s3_secret_key = YOUR_S3_SECRET_KEY

encoding_notify_url = hosting_url + '/notify'
encoding_notify_upload = hosting_url + '/encoded'
encoding_notify_error = hosting_url + '/error'

