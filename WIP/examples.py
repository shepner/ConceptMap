#save some bookmarks

from datetime import datetime
import uuid

body={
    'time': datetime.now(),
    'id': '1',
    'metadata': [
        {
            'title': 'Google stuff',
            'tag': ['web', 'search', 'email'],
            'url': [
                {
                    str(uuid.uuid4()): 'http://www.google.com',
                    str(uuid.uuid4()): 'https://drive.google.com',
                    str(uuid.uuid4()): 'https://gmail.com',
                },
            ],
        },
    ],
}

es.index(index, doc_type, body)

#clipped website

from datetime import datetime
import uuid

body={
    'time': datetime.now(),
    'id': '2',
    'metadata': [
        {
            'title': 'some page',
            'tag': ['web', 'interesting'],
            'file': [
                {
                    str(uuid.uuid4()): [{'path': '/some/path/here/', 'file': 'filename.html'}],
                    str(uuid.uuid4()): [{'path': '/some/path/here', 'file': 'image.png'}],
                },
            ],
            'url': [
                {
                    str(uuid.uuid4()): 'http://asdf.com',
                },
            ],
        },
    ],
}

es.index(index, doc_type, body)

#indexed file

from datetime import datetime
import uuid

body={
    'time': datetime.now(),
    'id': '3',
    'metadata': [
        {
            'file': [
                {
                    str(uuid.uuid4()): [{'path': '/some/path2/here/', 'file': 'filename.txt'}],
                },
            ],
        },
    ],
}

es.index(index, doc_type, body)

#link records 1 + 2

from datetime import datetime
import uuid

body={
    'time': datetime.now(),
    'id': '10',
    'metadata': [
        {
            'association': [
                {
                    str(uuid.uuid4()): ['1', '2', 'to']
                }
            ],
        },
    ],
}

es.index(index, doc_type, body)

print es.search(index)

print sorted(es.indices.get_aliases().keys())

print es.indices.delete(index)
print sorted(es.indices.get_aliases().keys())

body={
    'time': "asdf",
    'id': '1',
    'metadata': [
        {
            'title': 'Google stuff',
            'tag': ['web', 'search', 'email'],
            'url': [
                {
                    str(1234): 'http://www.google.com',
                    str(12345): 'https://drive.google.com',
                    str(12346): 'https://gmail.com',
                },
            ],
        },
    ],
}
body

#output
#{'id': '1',
# 'metadata': [{'tag': ['web', 'search', 'email'],
#   'title': 'Google stuff',
#   'url': [{'1234': 'http://www.google.com',
#     '12345': 'https://drive.google.com',
#     '12346': 'https://gmail.com'}]}],
# 'time': 'asdf'}
