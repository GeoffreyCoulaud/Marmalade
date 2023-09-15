from enum import Enum


class GroupUpdateType(str, Enum):
    CREATEGROUPDENIED = "CreateGroupDenied"
    GROUPDOESNOTEXIST = "GroupDoesNotExist"
    GROUPJOINED = "GroupJoined"
    GROUPLEFT = "GroupLeft"
    JOINGROUPDENIED = "JoinGroupDenied"
    LIBRARYACCESSDENIED = "LibraryAccessDenied"
    NOTINGROUP = "NotInGroup"
    PLAYQUEUE = "PlayQueue"
    STATEUPDATE = "StateUpdate"
    USERJOINED = "UserJoined"
    USERLEFT = "UserLeft"

    def __str__(self) -> str:
        return str(self.value)
