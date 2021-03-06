#all possible fields for a record

from datetime import datetime
import uuid

body={
    'time': datetime.now(),  #current time
    'id': str(uuid.uuid4()),  #UUID based on the host ID and current time
    'metadata': [
        {
            'title': '',
            'tag': [],
            'file': [
                {
                    str(uuid.uuid4()): [{'path': '', 'name': ''}],
                    str(uuid.uuid4()): [{'path': '', 'name': ''}],
                },
            ],
            'url': [
                {
                    str(uuid.uuid4()): '',
                    str(uuid.uuid4()): '',
                },
            ],
            'association': [
                {
                    # <from>, <to>, <arrow direction> ([to|from|none|both])
                    str(uuid.uuid4()): ['<from>', '<to>', 'to'],
                    str(uuid.uuid4()): ['<from>', '<to>', 'from'],
                    str(uuid.uuid4()): ['<from>', '<to>', 'none'],
                    str(uuid.uuid4()): ['<from>', '<to>', 'both'],
                }
            ],
        },
    ],
}

es.index(index, doc_type, body) #write to the DB and auto generate the DB ID number
