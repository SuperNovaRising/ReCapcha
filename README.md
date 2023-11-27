# ReCapcha
Re-imagining Captcha with AI

## Team Members

Chiung-Yi David Min Ishita Jindal Markus Mak Ram Sharma

## Project Overview 
reCAPTCHA is a security service introduced to differentiate human users from automated bots. It's primarily used to protect websites from spam and abuse. Here, we believe that reCAPTCHA is an old solution, especially in an era in which LLM could pass Turing Test. To prove that,

We developed a system to automatically identify the correct reCAPTCHA images using LLM image to text and semantic search capabilities. We then decided to use the knowledge developed to build a new reCAPTCHA using video (instead of static images) by semantically matching the prompt to the user response. Breaking Image Captcha with AI We showed that conventional image captcha is broken by leveraging AI capacity: We fetch each image in the grid We fetch the CAPTCHA challenge prompt, e.g. Click the images containing bike For each image, we use Salesforce CLIP model to generate the caption We then use Langhain to do semantic comparison between the generated caption and the CAPTCHA challenge. If the generated caption and the CAPTCHA challenge are similar enough, we identify the grid to be the target (TODO) The auto-click script “clicks” on the grid Break!

## Re-imaging Video Captcha using AI

We then redesigned the reCAPTCHA system using video instead of static images. We use a hidden prompt to generate a video using https://text-to-video.vercel.app/ We store the video using Supabase. We show the video to the user, asking the user to type in a response describing the image. We compare similarity between the hidden prompt using Together.AI and use score to test whether the user passes or not

## Future Work

We could further improve the video CAPTCHA! Imagine these videos to be 3x 1sec videos of ads, just like this one. (A video of Ads of MongoDB, Together AI, Langchain), which runs on loop. The question for the user to solve the Captcha could be “Click on the video of MongoDB”. AI would find it super hard to solve this Captcha because of the time element involved. This could be a great Captcha going forward - has a business model and is hard to crack by AI applications.

## Video Demo
https://www.canva.com/design/DAFzQrp4edA/rf3ejtVlyLvvCe8cu6BQSA/watch?utm_content=DAFzQrp4edA&utm_campaign=share_your_design&utm_medium=link&utm_source=shareyourdesignpanel
