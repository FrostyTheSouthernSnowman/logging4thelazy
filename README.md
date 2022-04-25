
<div id="top"></div>
<br />
<div align="center">

  <h1 align="center">Logs4theLazy</h1>

  <p align="center">
    Easily add logs to your python projects!
    <br />
    <a href="https://github.com/FrostyTheSouthernSnowman/logging4thelazy">View Demo</a>
    ·
    <a href="https://github.com/FrostyTheSouthernSnowman/logging4thelazy/issues">Report Bug</a>
    ·
    <a href="https://github.com/FrostyTheSouthernSnowman/logging4thelazy/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#overview">Overview</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Overview

Logs4theLazy allows you easily add detailed, descriptive, and well-structured logs to your project.

Logs4theLazy allows you to
* Define custom logging patterns
* Or you could just use a prebuilt one
* You can define the structure of your logs with LogFormats
* You can control where logs go through loggers

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

To install logs4thelazy, it is recommended to create a virtual environment and just use pip.

```bash
>>> python -m venv venv

>>> source venv/bin/activate

>>> pip install l4l
```

for Mac and Linux

or on Windows

```bash
>>> python -m venv venv

>>> source venv\Scripts\Activate.ps1

>>> pip install l4l
```

<!-- USAGE EXAMPLES -->
## Usage

To start using logs4thelazy, you must first have it [installed](#getting-started). After you install logs4thelazy, you must import it

```
import l4l
```

With logs4thelazy imported, you can use the basic default loggers

```
# l4l_example.py
import l4l

logger = l4l.BaseLogger(name="logger")

logger.log(l4l.from_value("Hello logging4thelazy world!"), stdout=True)
```

and then if you run it 

```bash
>>> python l4l_example.py
logger: List of all logs logged by logger, logger
logger: Hello logging4thelazy world!
```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Create basic working logger
- [ ] Create some extra logger classes that do things such as log to a file, log to a database, format the log, log with a trace-back, etc.
- [ ] Add some documentation

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make logs4thelazy better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Yosi Frost - yosi_frost@icloud.com

Project Link: [https://github.com/FrostyTheSouthernSnowman/logging4thelazy(https://github.com/FrostyTheSouthernSnowman/logging4thelazy)

<p align="right">(<a href="#top">back to top</a>)</p>
