
select u.username ,c.title, c.description from users u ,chats c; 

select u.username, c.title, ust.enter_datetime from users u, chats c, users_to_chats ust;

select c.title, c.owner_id, ust.enter_datetime from chats c, users_to_chats ust;

