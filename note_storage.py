import pickle


class Storage:
    """
    Storage with notes.
    It can be saved in file(cvs or pickle). It can be loaded from file.
    """

    def __init__(self, data=None, name=None, mode='pickle'):
        if name is None:
            if data is None:
                self.data = {}
            else:
                self.data = data
        else:
            if mode == 'pickle':
                with open(name, 'rb') as file:
                    self.data = pickle.load(file=file)
                    if data is not None:
                        self.data.update(data)
            elif mode == 'cvs':
                pass  # todo

    def get(self, key):
        return self.data[key]

    def set(self, key, record):
        self.data[key] = record

    def save(self, name, mode='pickle'):
        if mode == 'pickle':
            with open(name, 'wb') as file:
                pickle.dump(self.data, file=file)
        elif mode == 'cvs':
            pass  # todo

    def get_data(self):
        return self.data


if __name__ == '__main__':
    import os

    TEMP_FILE_NAME = 'test_note_storage'


    def compare_test(new_data, old_data, num_test):
        assert new_data == old_data, "Saved data and real data must be the same. Error in test number " + str(num_test)


    "First test"
    storage = Storage(data={
        5: 1,
        'cat': 'dog',
        '1': 1
    })
    storage.save(TEMP_FILE_NAME)
    old_data = storage.get_data()

    storage = Storage(name=TEMP_FILE_NAME)
    new_data = storage.get_data()
    compare_test(new_data, old_data, 1)

    "Second test"
    old_data['one'] = 'two'
    storage.set('one', 'two')
    storage.save(name=TEMP_FILE_NAME)

    storage = Storage(name=TEMP_FILE_NAME)
    new_data = storage.get_data()
    compare_test(new_data, old_data, 2)

    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), TEMP_FILE_NAME)
    os.remove(path=path)
