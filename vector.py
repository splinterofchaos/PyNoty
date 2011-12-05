
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

    def __sub__( self, other ):
        try:
            ret = Vector( [] )

            minRange = min( len(self), len(other) )
            maxRange = max( len(self), len(other) )

            for i in range( minRange ):
                ret.data.append( self[i] - other[i] )
            for i in range( minRange, maxRange ):
                if i > len( self ):
                    ret.data.append( -other[i] )
                else:
                    ret.data.append( self[i] )

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
    print 'a - b  =', a - b
    print 'b - a  =', b - a
