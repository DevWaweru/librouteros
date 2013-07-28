# -*- coding: UTF-8 -*-

class GenericWord( str ):


    def __repr__( self ):
        return '<{clsname} \'{word}\'>'.format( clsname = self.__class__.__name__, word = self )


###################
# Key value words
###################


class AttrWord( GenericWord ):
    '''
    This class represent word that starts with '='
    Available for reading and writing.
    '''


class ApiAttrWord( GenericWord ):
    '''
    Class that represents an api attribute word.
    Available for reading and writing.
    Such word starts with '.'.
    '''


###################
# No key value words
###################


class QueryWord( GenericWord ):
    '''
    Class that represents a query word.
    Query words start with '?' character.
    This word is available for writing only.
    '''


    def __eq__( self, other ):
        '''
        self == other
        '''
        other = self.typeCast( other )
        return QueryWord( '?={0}={1}'.format( self.name, other ) )

    def __ne__( self, other ):
        '''
        self != other
        '''
        other = self.typeCast( other )
        if other:
            return QueryWord( '?={0}={1}'.format( self.name, other ) )
        else:
            return QueryWord( '?>{0}={1}'.format( self.name, other ) )

    def __lt__( self, other ):
        '''
        self < other
        '''
        other = self.typeCast( other )
        return '?<{0}={1}'.format( self.name, other )

    def __gt__( self, other ):
        '''
        self > other
        '''
        other = self.typeCast( other )
        return QueryWord( '?>{0}={1}'.format( self.name, other ) )


class CmdWord( GenericWord ):
    '''
    Class that represents a command word.
    For example '/ip/service/print'
    This word is available for writing only.
    '''


class ReplyWord( GenericWord ):
    '''
    Class that represents a reply word. This word starts with '!' character.
    For example: !tag, !done, !re, !fatal.
    This word is available for reading only.
    '''


###################
# Unknown word type
###################

class UnkWord( GenericWord ):
    '''
    This class represent a word that is an unknown type.
    Received on response to '/quit' command
    '''



def getWordType( word ):
    '''
    Return an object word class based on leading characters.
    This method is used only when reading sentence.
    '''

    maping = {'=':AttrWord, '!': ReplyWord, '.':ApiAttrWord}
    return maping.get( word[0], UnkWord )

