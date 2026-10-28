# EnjoyStudying — Software Requirements Document (SRD)

## 1. App Name and Description

**App Name:** EnjoyStudying

**Description:** EnjoyStudying is an educational learning platform that helps high school and university students understand different subjects by watching educational videos organised by topic.

## 2. Problem Statement

High school and university students sometimes struggle to understand difficult topics through textbooks or classroom lessons alone. They may also find it difficult to locate educational videos that explain specific topics clearly.

EnjoyStudying aims to make learning easier and more enjoyable by organising educational videos according to subjects and topics, allowing students to find and watch relevant learning materials.

## 3. Target User Profile

The target users are:

- **High school students:** Students who want to understand school subjects, revise lessons, and prepare for examinations.
- **University students:** Students who want to improve their understanding of university subjects and learn difficult concepts.
- **Independent learners:** Students who prefer learning at their own pace using video explanations.

The application is designed for students who want a simple way to discover educational videos based on the topics they are studying.

## 4. Three MVP Features

### Feature 1: Subject and Topic Selection
Students can browse available subjects and select a specific topic they want to learn.

### Feature 2: Educational Video Library
Students can view a list of educational videos related to their selected topic and choose a video to watch.

### Feature 3: Video Learning Progress
Students can mark videos as completed so they can keep track of the topics they have studied.

## 5. Technology Stack and Justification

- **Python:** The main programming language used to develop the application because it is beginner-friendly and suitable for implementing the core features.
- **JSON:** Stores information about subjects, topics, video links, and completed videos in a simple format.
- **Visual Studio Code:** The development environment used to write, run, and test the Python program.
- **Web browser:** Opens educational video links so students can watch the videos online.

This technology stack is suitable for a first Python project because it is simple to implement, does not require a complex database, and can be expanded in the future.

## 6. Data Model

The application will store educational video information in a file named `videos.json`.

Each video record contains:

- `id`: A unique identifier for the video.
- `subject`: The subject the video belongs to.
- `topic`: The specific topic explained in the video.
- `title`: The title of the educational video.
- `url`: The link to the video.
- `completed`: A Boolean value indicating whether the student has completed the video.

Example JSON record:

    {
        "id": 1,
        "subject": "Biology",
        "topic": "Cell Structure",
        "title": "Introduction to Cell Structure",
        "url": "https://example.com/biology-cell-structure",
        "completed": false
    }

The example URL is a placeholder and must be replaced with a valid educational video link.

## 7. Risks and Mitigations

### Risk 1: Broken or Unavailable Video Links
Some videos may be removed or become unavailable.

**Mitigation:** Use reliable educational sources and periodically check whether video links are working.

### Risk 2: Incorrect or Low-Quality Learning Materials
Students may encounter videos that are inaccurate, confusing, or unsuitable for their level.

**Mitigation:** Select videos from reliable educational sources and organise them by subject, topic, and student level.

## 8. Success Metric

The first version of EnjoyStudying will be considered successful if at least 8 out of 10 test users can select a subject, find a relevant educational video, open the video, and mark it as completed without assistance during a usability test.
