
This is a DRAFT TRANSCRIPT from a live session at SRCCON 2014. This transcript should be considered provisional, and if you were in attendance (or spot an obvious error) we'd love your help fixing it. More information on SRCCON is available at http://srccon.org.  

Captioning by the wonderful people of White Coat Captioning, LLC  

whitecoatcaptioning.com  

SRCCON 2014  

Session 1 7-24-14, 1100-1200  

Franklin 2  

"There is no CMS"  

Session leader(s): Matt Boggie and Alexis Lloyd  

--  

>&gt;Hi, everyone.  Good morning.  Hi, everybody.  We're going to start.  


>&gt;Hello!  


>&gt;Would someone in the back not mind closing the door so that we don't get the noise from the outside, unless there are people coming in, in which case you're welcome to come in.  Hi.  I'm Alexis Lloyd, I'm a creative director at The Lab at the New York Times.  


>&gt;And I'm Matt, together we run databases.  We're here today to test a couple of hypotheses.  We've been looking at a tons of emphases from an architectural point of view, an organizational and technological point of view, and they suck.  And I think we all know that and that's why we're here.  We're going to go through a couple of reasons why we think this and what we can potentially do to get around that.  That part of the workshop today will be part of the participatory part of the workshop where we'll lay out the hypotheses and the questions.  And you'll break out into groups of at least five in these tables and from that point we'll talk about the approach but before that we want to make sure that we're on the same page about why we're here and what's going on next.  


>&gt;The heating and cooling is really loud.  So...  


>&gt;We will try to project.  


>&gt;We will try to project.  There's no amplification but we'll do our best.  At some point if we start dissipating, and you can't hear us, tell us to speak up.  I just want to start out with a few of show of hands, questions.  Who here had to switch CMSs in the past year?  In the past two years?  In the past three years?  Okay, so most of the people here have been through this pretty recently.  Who here has worked for an organization that has built or implemented multiple CMSs to support multiple products?  Okay.  Who here has written code to hack your CMSs so that you can do something that it doesn't want to do?  


>&gt;Of course.  


>&gt;Who here has published something outside of the bounds of your CMSs because it just won't do what you want it to do?  So we're all on the same page.  This is kind of where we are.  


>&gt;So as we look at the world that we're in today.  This is sort of the spectrum of stuff that we have been trying to use or forced to use or trying to implement depending on what we're doing.  As we've been looking at all of these different systems the thing that we find consistently is that CMSs tend to create more constraints than affordances.  They're walling you into a certain idea about what the world is, rather than letting you play and see what comes out of that.  Every day we work on these systems and the thing about is that they're built on decisions about our processes that were built years ago, even in those cases where you've implemented a new CMS for a reason.  You've gone through this process of saying, "I know what's wrong today.  I know all the things that I'm trying to fix.  So let's write them all down and build our systems because those are the things that'll fix it."  


>&gt;'Cause now we've got it right.  


>&gt;'Cause now we've got it right.  So nine months later, you've got nine months' worth of stuff in between --  


>&gt;I'll interrupt, but it's totally worth it.  He needs to come in to make the mic work.  


>&gt;Talk quietly amongst yourselves for just a second.  


>&gt;I'll just keep going, then.  


>&gt;We'll just keep talking louder.  


>&gt;So just to finish up on that thought.  A couple things.  So we're building on these systems based on the assumptions that we have today.  We've improved all of the depth, the process depth that comes out.  By the time it comes out we're already behind.  So we're building based on assumptions that are wrong, or at best, limiting and what we think.  So yeah, some assumptions that we were thinking about, specifically, some assumptions that they might enforce, relationships between data, text, assets, and presentations.  The way that we think about the products that we try to create.  The organizational process that goes into creating the news that we do.  Who's allowed to publish and under what conditions.  Who's allowed to edit and improve under what situations?  They often enforce some rules about visual design layouts.  The biggest thing I think that we can all agree on is that templates are both a blessing and a curse in a lot of ways.  Probably more often on the curse side.  And most importantly I think the big thing that we often forget when we talk about CMS is the base assumption, which is what is it that we're publishing and comes out over the overarching product?  Are you publishing a newspaper, or a website?  Or publishing into a mobile app and even more fine-grained level?  Are we publishing videos, text, data, graphs, and all of those are changing as we go through, and those are actually some of the biggest assumptions that we don't document very well as we're thinking about the systems.  


>&gt;So we have a couple of hypotheses about why this breaks.  And the fundamental problem here is that we build these as monoliths.  These are big, centralized systems that are trying to do too many things at once and like any kind of, all-in-one solution.  Like anyone here who's bought an all-in-one printer, it never does any of the individual things particularly well and by building all these things into one big monolithic centralized things, we also make it inflexible so that it can't adapt and change as organizational needs change.    


>And so, there's a list up here of that, you know, you could probably make, you know, three poster-sized things with more on there but this is an initial list that we made of, like, the different kinds of things that CMSs often are trying to do from text editing so asset management.  So workflow tracking, so archiving, and SEO, and publishing, and all these different tasks.  And it's trying to do all these things at once and, as a result, does in them really well -- none of them very well.  So our hypothesis is that we need this not this.  We need not a monolith, but all these different tools.  We have tools for all these different things.  Everyone has a text editor they like.  People who work with photo editors, there are tools they prefer to use.  There are SEO tools that people prefer to use and on and on and on.  So the question is, why do we need CMS tools?  Why can't we enable people to use the best tools available for each task and allow those tools to collaborate or communicate through a very minimal piece of tool or centralization?  And that system should be modular and flexible so that it should allow for the rapid adaptation that we need.    


>And so we've been thinking about this.  This is our hypothesis at a high level:  Is that, rather than one centralized thing we need a set of pieces loosely joined.  But there's still a bunch of questions that that brings up about, you know, what is the minimal amount of stuff that you need to hold these things together.  Like, what is a CMS?  Why do we need it?  What would a not-CMS look like, and also what does that imply for the rest of the organization?  So one of the interesting things that butted up against in a lot of the arguments that we've been having in our review lab about this is -- our questions about, this is kind of where technical design and organizational process butt up against each other and there are these really interesting places where one influences the other.  


>&gt;So how many of you know about Sorites' Paradox?  So Sorites is Greek for "heap."  So starting from bad principles, you can ask questions, here's a pile of sand.  If I take a grain of sand away is it still a pile?  Yes, so if you use a mathematical proof to that, one grain is a pile, negative grains are in fact a pile, so we don't buy that at all.  So there comes a point semantically, where the "pile" stops being a "pile."  If that's our pile, and that's our list of stuff, and another page of two of stuff is a pile as well.  Is CMS -- what is the minimal amount of stuff that we can create that stitches all these things together that maybe isn't yet considered a pile?  What would that look like if I'm editing using something like Sublime Text, or I'm measuring my photos in Lightroom, or Aperture?  And like Alexis said, that stuff is an organizational process.  So knowing the room here, we've got technologists, we've got writers, organizational people, people who have been through the system.    


>So this really is the task that we're set up with today:  How do we take that heap and break it down into something so that it is down into something so that it's quasi-recognizable, but maybe knowledge still considered a pile.  So that's what we're going to do.  It's 11:15 so what I wanted to do was take about 20 minutes, circulate through and start talking about this hypothesis to see if we agree with it, to see if there are additions we want to add to it.  And start to think about the nitty-gritty on how to implement this.  So what are the alternatives that you can develop to having the one centralized system?  Is it possible to allow or facilitate the use of preferred tools?  And in this case, you might go down the road of choosing one and building a buttress to it.  Or you might allow for an architecture that allows lots of things to talk to other things.  And if -- so if you can do that, what is the minimal amount of centralization that's required, organizationally, and technically, to actually create a product?  And as you go through this think a lot about process and the technology that you would to glue that together.  But perhaps, more importantly, as you do this as a group, closely document the assumptions that you're making.  What is it that you're making?  Is it a site, is it a paper, is it a mobile web app, is it all of those things?  What are your assets?  Who are your users?  What are your outputs?  


>&gt;How big is your organization?  


>&gt;How big is your organization?  We're going to go around from table to table at the end talking about the solutions that you've outlined, and start potentially focusing on holes in them.  What if you were to add a new product on?  Or what if you suddenly merged with another company, how would you get around some of those kinds of questions, both organizationally and technically, logistically?  We've got a lot of people standing up in the back and open tables up front.  And as best you can, try and get into -- I guess we'll have an sixth table -- wherever there's a table, there's a group and there'll be a "tableless" nexus group of people back there.  Alexis and I will be circulating around the room to answer sort of logistical questions.  It's a centrally open ended activity and I hope you title as a challenge rather than a fear-based thing.  So you can define this as best the team has the skills to do.  As technical as you want, as organizational as you want.  Any questions before we go?  Really?  That made sense?  Awesome.  Great.  Break into your groups and start.  If you need supplies we have Post-Its over here.  


>[ Discussion Groups ]  


>&gt;We have six groups and we want to talk about either about the organization or the --  


>&gt;Is everyone hear?  


>&gt;Can everyone hear Matt a little better now?  


>&gt;This seems to kind of work so I'm going to pass this around to those groups that are presenting.  By now, pick a person to be your guinea pig.  Each team will have about three minutes to just talk a little bit about what they've talked about, some of the solutions they've come up with, some of the challenges that are out there.  We do have some other questions along the way and that should get us through here.  So we'll start out here.  


>&gt;Good, so, we totally solved all these problems.  So you guys, should just -- all right.  We got it all here on this notebook.  This solves all the problems.  So no, we didn't solve all of the problems, actually we didn't even solve any of the problems.  We were overall concerned about how people put things into the CMS, assuming that all of the rest of you would be concerned about what it is stored and what it is outputted.  So we'll just let you guys handle that part.  So we were really interested in how people, or how a reporter, or a photographer or someone who makes video or somebody who, like, does a video project, what does a look like what they file into an awesome, "that-world CMS" that we were inventing, right?  So the thing that we kind of stuck on was we need together to go reach people that they are.  So if we have people that like to file on Word documents, we should have them file on Word documents, if they want to email the story to somebody, they should continue emailing to somebody.  And we should figure out some technology that passes it to some agnostic thing in the middle that will store it and can and that's where you guys are probably come up with really good ideas.  So we were very fascinated with listing the different types of content that our news organizations produce as a result of their deliberations and hard work.  So Tyler works at NPR and they produce audio.  There's pieces of audio that are made shorter, or -- and binary is really hard to do in a content management system so that's, like, one of the stumbling blocks that will make your life really difficult, and just imagine that times a billion with photographs and video, and all of these things that are non-text, that you still need to be able to edit and show differences in.  And then we have all these different forms of text and, like, data, and metadata about things that need to get put in so that's the part where we just decided what we really need is a really good messaging system full of u-bots that interprets our behavior and.  We decided that was super hard so what we wanted to do was fire the editors and just have a crew of people doing all the time, what they want to do.  That's about the part where we broke down, and then it reverted into a state of nature.  I'm really hoping that you guys have much better solutions than us.  So yeah, we basically -- so we came out of this with humans and robots are really good but we should all work together.  And it would be better if we had more sentience, generally.  


>&gt;Wow, okay.  Lots of open questions there.  I'm going to keep going through.  We'll come to the second table.  Who wants to tell us where you landed.  


>&gt;You can do it.  


>&gt;I do not want to do it.  


>&gt;You wrote it down.  


>&gt;We'll fill in.  


>&gt;So I don't know how to follow up that.  We do have union corns and pandas, and cats in ours.  So our basic conversation was about storing the content, the content libraries should be separate than the content-creation process, some related to you all.  We believe that the content creators should do that wherever they would like to do that.  And so, the content creators, we need to build tools that actually get that content from them and that is the problem right now.  So we talked a lot about how people used Microsoft Word, or Sublime, or whatever text editor they want to I don't say and we're trying to force people to create -- we're trying to force people to create content within the CMS.  And so then the content library would just have an API that could push to whatever, editing interface.  The magical robots choose to push it to.  So you could have an different mobile editor, a different print editor and then that would push to all of the screens in the world.  So, all 26 different sizes.  Do you guys want to add anything?  


>&gt;That sounds good.  


>&gt;Move onto unicorns?  Why do they come in?  


>&gt;They're in the middle.  


>&gt;They're stored in the content library, mostly.  And then they're released when someone's sad. I think.  


>&gt;I think the big thing for us was just this idea of this should be a content library that stores structured data, that stores your content as structure structured data instead of oh here's an article and it's finished and it's got images in it.  So there's articles, and there's photos and then there's charts of everything you do and then it's someone else's job later with a different tool to piece that together to what it should be for print and then for mobile, and then for different kinds of websites so it's not one thing that's edited in one CMS.  They're just pieces of content stored in a library and then really smart editors later can put them together in different ways.  


>&gt;That sounds pretty good before we go then the next -- before we go onto the next.  We've heard a lot about content creation at the level of the article or the asset.  I'll put this to all the groups has anybody thought about information at the subasset level.  There's some coverage, for example of Circa's CMSs for quote-level attributions that could later be retrieved?  


>&gt;We were talking about how CMSs are all right now based around the idea that there's a slightly big body types and actually it would make more sense to have a list of objects, effectively be that a paragraph, or a part of a paragraph or one graphic so that it becomes something that these guys were saying so that it becomes structured data and assets.  


>&gt;And then the challenge becomes how do you not make that look like a big, huge, behemoth form?  


>&gt;Would you go mind if we listened to their solution and then came back to you?  Why don't you continue on a little bit?  


>&gt;Okay, so yeah, um, so, we sort of started thinking about CMSs as a monolith, and I think we originally made the CMSs today aren't stupid it was just that there was no way that you would anticipate the kind of things that we had today.  So what about the CMS is basically an API, and what is the core, smallest level that you could rely on that would not end up tripping up you up in the future so we're sort of talking about probably the ideas that you guys had.  But the idea is that it's very modular.  So what it's really called is a CPS store and then there's various modules that plugged and took data out of it.  So we started to think about the core users and security because that seems like that's something that's unite universal and then there's needs to be versioning of whatever the structure of the data is, and there would need to be some kind of eventing system.  So my web publishing module, or my A publishing module can listen, and hopefully just sort of end up with this seamless data flow, and the responsibilities of very centralized in these tiny modules.  


>&gt;And we also talked about how the, like, how we would display content and how that would be decided and how that would be organized would be separate.  And how you bring content into the system, how you author it, would also be separate.  


>&gt;Okay.  Any thoughts on that approach?  


>&gt;So I have a quick question, sort of for the room based on what people have said so far which is a basically if people see storage as a centralized part here, or whether storage is also a part that could become modular?  


>&gt;You know, I think there's a level at which it doesn't matter, right, you know, if we have a bunch of tools that could all talk to each other, they could be responsible for storing their own data as long as they all speak a common language.  So what common storage becomes is a common language.  That's what we talked about, at least.  


>&gt;Do you want to keep going, then?  


>&gt;Someone else. I was just answering a single question.  


>&gt;Um, well, you know, as journalism gets, you know, increasingly interactive, the question becomes, you know, what is the unit of content?  And I'm sure everybody here is familiar with the snowfall project that the Times put out a year, a year and a half ago.  You know, really interactive one that won the Pulitzer Prize.  There's a wall on the 50th floor for all the prizes they've done.  And there's a plaque.  You know, what is in the content at that point?  


>&gt;But the question that you asked, I thought that was really interesting was that, like, what is -- okay -- so the question that got asked which was really interesting was what is Snowfall going to look like in 150 years?  Which is really cool because it's kind of like you think about what the Times or any of our other papers look like whenever they opened, you know, in the late 1800's, so 19 hundreds, we can look back and see the same thing but with the development of technology, like, many technologies even if you look back ten years, you're looking back at, like, Flash interactives, and what is that going to look like in 50 years, and how are we going to archive these things, and how how are we going to plan for that obsolescence and Alexis asked a really good question of this is, what is the need of standardization?  So what can that serve for us?  We kind of went back and forth a lot about, like, two taxonomy, or to not taxonomy and what does that mean?  And, you know, what does tagging mean for us?  Is it possible for us to standardize tagging the way that people in, say, the audio world, that you just brought up have been able to do is that possible for journalism and if so, who is responsibility is that?  Is it WordPress' responsibility as the CMS creator, or is it our responsibility as technologists and edittorily staff in the newspaper to define that standardization?  That's about as far as I got.  


>&gt;Some of us said, that tagging is not possible.  Fool's errand but there's no other choice, I think.  


>&gt;I think, it's a 50/50 at this point.  


>&gt;But the 150 year point is interesting.  The tag point as well.  So we have tags about things like molasses floods which is kind of amazing.  Why don't we go back here.  Volunteers?  


>&gt;Okay, so we started trying to define fundamentals, basically, and how do you start collapsing four layers that do one integrated thing:  Creation, importation, and display.  And you know, where are those points at which we can sort of merge or integrate those things or just sort of collapse them?  And then, also defining, you know, what are the CMS limitations versus the template limitation?  You know, harass with we interpreting as CMS problems that are actually displayed problems with our templates that are actually fixable on that end?  Also thinking about the users of that CMS in layers.  You've got a technical layer of builders and support.  Backend editorial, or whoever will all need to use the same thing on the backend.  But also customers and leaders at the final point.  And then how much do you want to integrate user customizability and what does that introduce if you're trying to sort of have a centralized repo, or library of various sort of content types.  If you want the user to be able to customize display, or priority, how does that factor into what you're building on the backend?  We didn't get as far as solutions more than just sort of talking these things out, and defining problems. Did I miss anything?  


>&gt;Um... I'll take that one.  So we have a list up here of different features.  I think you just went through four sort of overarching groups of features:  Creation, importation, publication, and display.  Are there other major pieces that we should also be considering along the way other than those four?  I think we can probably debate taxonomy to the end of it.  Storage is one.  


>&gt;So, there are some categories of content that I don't really -- that don't necessarily have any of these components in the system where there's, like, say you build an app, that app needs to control the entire experience.  So it's not, in many ways it's not as useful as an abstract in a publishing system for display.  It's not necessarily usable in terms of categorization, but there's still stuff that the CMSs supposes as content making it discoverable, and making it "interactivable."  


>&gt;And you know, starting fundamentals is a great way to think about this.  What do the things that we need to make, where do they go, what do we do to them?  All three of those answers have effects on the other questions.  


>&gt;And how many people need to do things, too.  


>&gt;Right, who are your users.  Last group over here?  


>&gt;So... so basically we've basically come up with this called, we're calling it moveable type.  So actually we came up with a lot of problems, like, you know, and we started bring asking questions like:  Are we building this from scratch or are we starting from something that already exists.  Obviously if you're starting with something that already exists.  It's probably easier.  And then you started from scratch and it's going to take even longer.  So we go back to the existing tools.  And then the idea is, do you do things very well in one place, or do you do things really, super well in silence?  And the problem with silos is that then how do you tie them together because content even like a content like a list is 40 different pieces of content together as one.  It's not just, like, this one big thing.  It's a post, and then ten child posts and then how do you search for it?  And how do do you do all these things so we came back to little pieces like how the Internet originally started?  Somebody built a shipping software in VB and then somebody else built a billing software in VB, and it's like, I have no idea how to get those talk together.  And I know Perl until they change and then the duct tape breaks.  And then who gets to build these and maintain these?  And it's all of us.  So I just want to apologize and then we came up with the gravity theory which was, what we really want is, something really big in the center that you can just throw stuff in it, and then it'll just orbit around it just fine and then throw stuff.  And so you've got this whole solar system of content where you've got, like, your "moon CMS" part roaming around, the "Earth CMS" part, and then they're all tied together by this massive sun in the center and so we just played God for a little bit.  


>&gt;Wow...  


>&gt;God, CMS is trademarked, too.  


>&gt;Good point.  So we have literally one minute left.  So just to wrap up.  I love that ending and I was sort of getting halfway through with some of the other answers and just this experience of sitting for an hour and trying to redesign the most core process of any of our organizations is actually obviously a fool's errand but I think it does point to a central conflict that we're all dealing with here, which is that we're all trying to play God.  We are trying to define the solution for dozens of different processes and outcomes in a very complicated organization with hundreds, if not thousands of people contributing to them.  Why would ten people around a table be able to do that?  So what are some of the ways that we can enable better does thed thinking?  Can we build something that somebody can plug into so that we can make a system so that it works with everybody else and it doesn't need to go through a big, centralized committee to decide that.  These are difficult questions.  There are many different problems involved in them.  It wasn't meant to solve the whole world today.  But hopefully you can start thinking about these questions as you build your next project.  Great.  


>&gt;More of this tomorrow at 3:00 in the same room.  


>&gt;Yeah, you can make that CMS that makes other CMSs.  

