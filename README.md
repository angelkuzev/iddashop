# iddashop

This is my first personal project. Its made using Django for the server part and MaterializeCSS for the design.

Iddashop is an online clothing store. 
Each clothing item has a name, description, price, size (S, M and L), quantity of each size and a category.
There are 3 types of users: normal user, staff and admin.

When accessing the site without a logged in user you can only browse the available items and see their details.
Logged in users have a cart and can order items.
Staff and admin users have a panel with their permissions.

Staff users can add and edit items.
Staff users can add categories
Staff users can accept orders and set a date of expected arrival.

The admin also has all staff permissions.
The admin can manage the staff. (give or revoke staff permissions)
