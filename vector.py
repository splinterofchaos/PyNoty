
class Vector:
    def __init__( self, vec ):
        self.data = vec

    # Python functions.
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

    def __add__( self, other ):
        try:
            if len(self) < len(other):
                minVec = self
                maxVec = other
            else:
                minVec = other
                maxVec = self

            ret = Vector( [] )

            for i in range( len(minVec) ):
                ret.data.append( minVec[i] + maxVec[i] )
            for i in range( len(minVec), len(maxVec) ):
                ret.data.append( maxVec[i] )

            return ret
        except TypeError:
            raise TypeError
                

if __name__ == '__main__':
    a = Vector( [1,2] )
    b = Vector( [2,1] )
    a[0] = 5
    print 'a      =', a
    print 'b      =', b
    print 'len(a) =', len( a )
    print 'a[1]   =', a[1]
    print 'a + b  =', a + b
