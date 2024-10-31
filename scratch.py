def restore_documents(originals, backups):
    return set(
        map(
            lambda x: x.upper(),
            (filter(lambda x: not x.isdigit(), originals + backups)),
        )
    )
