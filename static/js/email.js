(function sendMail(contactForm) {
      emailjs.init(" user_t0zUP8ySyXRy1bOf7ZHEA");   })();
               emailjs.send("outlook", "loader_media", )
               name: "Aaron",
               notes: "The project that I want is..."
                  })
              })();

    .then(
        function(response) {
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
    return false;  // To block from loading a new page
}
