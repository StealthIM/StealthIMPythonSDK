from StealthIM import User, apis
from StealthIM.apis.group import GroupMember, GroupInfoResult, GroupPublicInfoResult, InviteGroupResult, \
    GroupMemberType, SetMemberRoleResult, KickMemberResult, ChangeGroupNameResult, ChangeGroupPasswordResult
from StealthIM.apis.message import SendMessageResult


class Group:
    def __init__(self, user: User, group_id: int):
        self.user = user
        self.group_id = group_id

    @classmethod
    async def create(cls, user: User, group_name: str) -> "Group":
        """
        Create a new Group.

        Args:
            user (User): The user to create.
            group_name (str): The name of the group.

        Returns:
            Group: The created group.

        Raises:
            RuntimeError: If the request failed.
        """
        res = await apis.group.create_group(user.server.url, user.session, group_name)
        if res.result.code != 800:
            raise RuntimeError(res.result.msg)
        return cls(user, res.groupid)

    @classmethod
    async def join(cls, user: User, group_id: int, password: str) -> "Group":
        """
        Join a Group.

        Args:
            user (User): The user to join.
            group_id (int): The ID of the group.
            password (str): The password.

        Returns:
            Group: The joined group.

        Raises:
            RuntimeError: If the request failed.
        """
        res = await apis.group.join_group(user.server.url, user.session, group_id, password)
        if res.result.code != 800:
            raise RuntimeError(res.result.msg)
        return cls(user, group_id)

    async def get_members(self) -> GroupInfoResult:
        """
        Get members of the group.

        Returns:
            Members: The members of the group.
        """
        return await apis.group.get_group_info(self.user.server.url, self.user.session, self.group_id)

    async def get_info(self) -> GroupPublicInfoResult:
        """
        Get info of the group.

        Returns:
            Info: The info of the group.
        """
        return await apis.group.get_group_public_info(self.user.server.url, self.user.session, self.group_id)

    async def invite(self, username: str) -> InviteGroupResult:
        return await apis.group.invite_group(self.user.server.url, self.user.session, self.group_id, username)

    async def set_member_role(self, username: str, role: GroupMemberType) -> SetMemberRoleResult:
        return await apis.group.set_user_role(self.user.server.url, self.user.session, self.group_id, username, role)

    async def kick(self, username: str) -> KickMemberResult:
        return await apis.group.kick_user(self.user.server.url, self.user.session, self.group_id, username)

    async def change_name(self, new_name: str) -> ChangeGroupNameResult:
        return await apis.group.change_group_name(self.user.server.url, self.user.session, self.group_id, new_name)

    async def change_password(self, new_password: str) -> ChangeGroupPasswordResult:
        return await apis.group.change_group_password(self.user.server.url, self.user.session, self.group_id, new_password)

    async def send_text(self, message: str) -> SendMessageResult:
        return await apis.message.send_message(
            self.user.server.url,
            self.user.session,
            self.group_id,
            message,
            apis.message.MessageType.Text
        )

    async def receive_text(self):
        gen = apis.message.get_message(
            self.user.server.url,
            self.user.session,
            self.group_id,
            0,
            0
        )
        async for data in gen:
            yield data