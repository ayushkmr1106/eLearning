from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'storageaccquadsquad' # Must be replaced by your <storage_account_name>
    account_key = 'SvWV0tfr94YrqKp+9EmwKJ+T2P7a7XFgTAq32r9t1kYxRbINzygoUbq8oFEIoLX/Mi0XOU6T+OyX+ASt2oPzfQ==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'storageaccquadsquad' # Must be replaced by your storage_account_name
    account_key = 'SvWV0tfr94YrqKp+9EmwKJ+T2P7a7XFgTAq32r9t1kYxRbINzygoUbq8oFEIoLX/Mi0XOU6T+OyX+ASt2oPzfQ==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None