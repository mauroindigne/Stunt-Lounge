# Stunt Lounge

Stunt Lounge is a website database that stores youtube embedded videos and more information. The reason I decided to create this website was because I am a professional motorbike freestyle stunt rider. I wanted a database where I or others could store videos from youtube based on the motorbike models. This is because people who are new to the stunt riding scene would like to find videos of a motorbike they have or would like to use and this gives them a database built by fellow riders. Originally I would use youtube's “Liked” videos section to save videos I liked. However I wanted a more “Stunt Bike Vibe” and something that would categories which brands I picked, and that is when I created Stunt lounge. 

Stunt lounge is a free to use database of stunt videos that uses the CRUD functionality. You can add your favorite stunt videos from youtube to this database by clicking the “Add Video” button then adding the last 11 characters of your URL from youtube and giving it a title and selecting which motorbike is featured in this video. Then the videos will be displayed in an easy to view embedded video blocks that flows well with whatever device you are viewing it on. These videos can also be categorized by Brand name by clicking on the “Search by Brand” button this helps narrow down the videos and help the user find the video they want. 

- [Website](https://stunt-lounge.herokuapp.com/)

 
## UX

My main goal was to create a simple website for stunt riders or bikers to view and add youtube videos that they enjoy and want to share with the world, while having a clean minimalistic modern design that was easy for users to navigate. With this in mind I started with a simple clean navbar. This included a logo with the website's name that could be clicked to send the user back to the home page. Next came the layout of the videos, I added a fair amount of breathing space to the sides of the home page for the desktop view (limiting the videos to 3 columns) slowly switching to 2 for smaller devices and then finally 1 column for mobile devices. This keeps the website clean and from reshaping the look of the website. Next I added the ability to search for videos by the brand of the bike. This will categories the videos by the brand of motor bike that users have selected while adding videos to the page. 


- As a user, i want to save stunt videos , so i can view them easily.

- As a user, I want to be able to sort videos by the brand of the bike, so that I can find videos for a specific brand of motorbike.

- As a user, i want to be able to delete videos, so that there are not videos that shouldnt be included.

- As a user, I want to be able to update and edit video information, so that everything can stay upto date.

- As a user, I want to have a clean, easy to use navbar, so that going from page to page doesn't include clicking back on the browser. 

- As a user, I want to have a simple to play video format so i don't have to open a new tab to view videos.


The wireframes are found inside the wireframe [directory](../wireframes/), here you will find my mockup designs that i created on google slides, for the home, about and “search by brand” pages.

## Features
 
### Existing Features

- CRUD functionality 

- Create - The user has the ability to create and add new data into the database via the "Add Video" button. This then sends the information
that the user put into the form and creates a new file within the database with all the information about this video. Then the user is redirected back to the home 
screen where the info they filled in is displayed on the screen. 

- Read - The user has the ability to search for a file through the "Search by brand" seaction. This organized all the videos and creates a new page with only 
videos of the brand selected.

- Update - The user has the ablilty to update data from the database via the pen icon on each of the videos. Furthermore once at the "update video"
area, the specific data that was clicked is pulled from the database and put on display on the form to help the user more.

- Delete - The user can also delete information from the database by clicking on the trashcan icon next to each induvidual box.

- Catagorising videos - The user has the ability to view videos by the brand of the motorbike by clicking on the "search by brand" button on the navbar. What this does is grab all the videos that have the value of that brand in the Brand seatction on MongoDB and load those into a template for that brand.

- Error 404 page - I created a custom error 404 page by importing flasks "abort" file. This allowed the page to be redirected to a 404 page that also has a button to redirect the user back to the home page. The reason i wanted a custom "error 404" page is because it looks much more offical and adds that extra layer to really complete a website.  

- Custom Tab Icon - I created and added a tab icon to the page, while it is a samll touch it creates a more complete website.

### Features Left to Implement

- Auto Url - I really wanted the user to be able paste any URL from youtube into the form and for the code to change this into a /embedded/ link every time. This is because currently the user has to manually add the last 11 characters from the url to allow the website to work. In the future I will study RegEx more to get an understanding to be able to implement this feature so that it can read the url and replace whatever url comes before those 11 characters with the embedded form. This will smooth out the UX and lead to an overall higher quality website.

## Technologies Used

- [HTML](https://en.wikipedia.org/wiki/HTML) 
    - to create the framework of my website.
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    - to design the look of the website and colors.
- [Javascript](https://en.wikipedia.org/wiki/JavaScript)
    - for bootstrap
- [python](https://www.python.org/) 
    - to change the layout of the website using base.html
- [Font-awsome](http://fontawesome.com/)
- [fonts.googleapis](https://fonts.google.com/)
- [MongoDB](https://www.mongodb.com/)
    - to store all the data 

## Testing

- linking pages - I spent lots of time making sure there was a clear and working link between all pages. I had to go back and forth on pages to make sure that the user did not have any pages that lead to nothing or that wouldn't allow them to easily go back to the home page.

- error 404 pages -  Creating a custom Error 404 page was an important part for me, as it makes your website look more professional and complete. Also to improve the UX i added a “back to home” button on the 404 page just in case the user does not know that they can press the brand title. The Error 404 page path was helped by Flasks “abort” file.

- database Testing - This testing involved creating multiple "test" videos to make sure that what was being created was indeed going to the database and being pulled back on to the page. For example I had to test that when the user wants to edit a video that they are presented with the previous title, brand name, url and model. So that the user knows that they are indeed editing the correct video. Furthermore I had to test to see that all information was being correctly added to the desired collection on mongodb. 

- Screen sizing for mobile devices - As usual a lot of my time testing was spent making sure that the website was equally attractive on all mobile devices and screen sizes. This involved shrinking the (Stunt Lounge) title and logo to move and shrink for more narrow devices. I also had to spend time to make sure that each video block had an acceptable amount of breathing space around the video while not created to much wasted space.

### Bugs

One quite interesting bug that you may notice is when hovering over the "edit" and "delete" icons is that it does not apply the hover style (add red line under to indicate its clickable) to the icon currently being hovered over, but instead seems to randomly give this affect to another icon from another video block completely. This may be due to the fact that all the videos are just a “for loop” but i'm not quite sure and haven't been able to figure this out.

## Deployment

This site is hosted using Heroku pages, deployed directly from the master branch. (https://stunt-lounge.herokuapp.com/)

## Credits

- Youtube videos

- Bootstrap Navbar

### Content



### Media

- The Photo is my own

- Videos come from Youtube(https://www.youtube.com/)

### Acknowledgments

- I was inspired to make this website because of how i spend lots of time watching these video, i wanted a place to store them.