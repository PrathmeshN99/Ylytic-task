A REST API ( https://app.ylytic.com/ylytic/test ) is exposed to fetch comments from a
YouTube video. Each comment has 5 fields: at, author, like, reply, and text. These fields
respectively mean the date of the comment, who posted the comment, number of likes of
that comment, number of replies to that comment, and comment text.
Your goal is to create a search API on top of the existing API which will serve the below
set of requirements:
1. Comments can be searched with author name (search_author field) 2.
Comments can be searched with a date range (at_from and at_to search fields) 3.
Comments can be searched with reply and like count range (like_from, like_to,
reply_from, reply_to fields)
4. Comments can be searched with a search string in the text field.
(seach_text) 5. All the above searches can be done within the same request
as well.
E.g.:
1. API: <base-url>/search?search_author=Fredrick&at_from=01-01-2023&at_to=01-02-
2023&like_from=0&like_to=5&reply_from=0&reply_to=5&seach_text=economic
This will return all comments where the author name contains ‘Fredrick’; and the comment
is posted between dates 1 Jan 23 and 1 Feb 23; and a number of likes is between 0 to 5,
and a number of replies are between 0 to 5, and the comment text contains ‘economic’
2. <base-url>/search?search_author=Fredrick
This will return all comments where the author name contains Fredrick
Important points:
* Solution needs to be done using Flask framework in python.

* Host your solution to Amazon Lambda and share demo APIs.
* Please send across the codebase. You can also share the git repo link.
