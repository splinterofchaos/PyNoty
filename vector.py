
class Vector:
    def __init__( self, vec ):
        self.data = vec

    def __getitem__( self, key ):
        return self.data[ key ]
    def __setitem__( self, key, value ):
        self.data[ key ] = value

    def __len__( self ):
        return len( self.data )

    def __str__( self ):
        string = '< '
        for axis in self.data:
            string += str(axis) + ', '
        
        # Get rid of the last ', '.
        string = string[ : -2 ]
        
        return string + ' >'

if __name__ == '__main__':
    a = Vector( [1,2] )
    print a
