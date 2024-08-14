
select u.username from users u
right join chats c
on u.id = c.id
where c.id != c.owner_id;

select u.username from users u
inner join users_to_chats ust
on u.id = ust.user_id
where ust.chat_id = Null;

select u.username, c.title, c.description from users u
inner join chats c
on u.id = c.id
order by c.title desc;

select u.username, c.title, ust.enter_datetime
from users u
join chats c
on u.id = c.id
join users_to_chats ust
on u.id = ust. user_id
order by ust.enter_datetime desc;






