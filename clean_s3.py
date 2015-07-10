import boto

s3 = boto.connect_s3()

buckets = s3.get_all_buckets()


def empty_bucket(b):
    for version in b.list_versions():
        b.delete_key(version.name, version_id=version.version_id)


for b in buckets:
    empty_bucket(b)
    b.delete()
    print 'deleted bucket: {b}'.format(b=b)
