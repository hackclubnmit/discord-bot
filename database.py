import json
from google.cloud import firestore
import google.cloud.exceptions

def initdb():
    '''
    Subject to Removal
    This Function serves no real purpose
    '''
    # [START quickstart_new_instance]
    from google.cloud import firestore

    # Project ID is determined by the GCLOUD_PROJECT environment variable
    # https://firebase.google.com/docs/admin/setup#initialize-sdk
    db = firestore.Client()
    # [END quickstart_new_instance]

    return db

def giveCredits(name):
    '''
    Update the reputation of a user in firestore
    '''
    db = firestore.Client()
    # [START update_data_transaction]
    transaction = db.transaction()
    user_ref = db.collection(u'users').document(u'{}'.format(name))

    @firestore.transactional
    def update_in_transaction(transaction, user_ref):
        snapshot = user_ref.get(transaction=transaction)
        transaction.update(user_ref, {
            u'reputation': snapshot.get(u'reputation') + 1
        })

    try:
        update_in_transaction(transaction, user_ref)
        return True

    except google.cloud.exceptions.NotFound:
        print(f"Couldn't modify {name} rep")
        return False

def getCredits(name):
    '''
    Retrieve the rep of a user from firestore
    '''
    db = firestore.Client()
    # [START update_data_transaction]
    user_ref = db.collection(u'users').document(u'{}'.format(name))
    doc = user_ref.get().to_dict()
    if doc != None:
        rep = doc['reputation']
        return rep
    else:
        return -1
