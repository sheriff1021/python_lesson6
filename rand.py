import random
import string
class GetPassword():
    def GetInt(self):
        numba=random.randint(1001,9999)
        return str(numba)
    def GetString(self):
        length=4
        letters=string.ascii_lowercase
        result_str=''.join(random.choice(letters) for i in range(length))
        return result_str
