##What are automated tests?
Tests are routines that check the operation of your code.
Testing operates at different levels. Some tests might apply to a tiny detail (does a particular model method return values as expected?) while others examine the overall operation of the software (does a sequence of user inputs on the site produce the desired result?). That’s no different from the kind of testing you did earlier in Tutorial 2, using the shell to examine the behavior of a method, or running the application and entering data to check how it behaves.
What’s different in automated tests is that the testing work is done for you by the system. You create a set of tests once, and then as you make changes to your app, you can check that your code still works as you originally intended, without having to perform time consuming manual testing.

##Why you need to create tests
So why create tests, and why now?
You may feel that you have quite enough on your plate just learning Python/Django, and having yet another thing to learn and do may seem overwhelming and perhaps unnecessary. After all, our polls application is working quite happily now; going through the trouble of creating automated tests is not going to make it work any better. If creating the polls application is the last bit of Django programming you will ever do, then true, you don’t need to know how to create automated tests. But, if that’s not the case, now is an excellent time to learn.

##Tests will save you time
Up to a certain point, ‘checking that it seems to work’ will be a satisfactory test. In a more sophisticated application, you might have dozens of complex interactions between components.
A change in any of those components could have unexpected consequences on the application’s behavior. Checking that it still ‘seems to work’ could mean running through your code’s functionality with twenty different variations of your test data to make sure you haven’t broken something - not a good use of your time.
That’s especially true when automated tests could do this for you in seconds. If something’s gone wrong, tests will also assist in identifying the code that’s causing the unexpected behavior.
Sometimes it may seem a chore to tear yourself away from your productive, creative programming work to face the unglamorous and unexciting business of writing tests, particularly when you know your code is working properly.
However, the task of writing tests is a lot more fulfilling than spending hours testing your application manually or trying to identify the cause of a newly-introduced problem.

##Tests don’t just identify problems, they prevent them
It’s a mistake to think of tests merely as a negative aspect of development.
Without tests, the purpose or intended behavior of an application might be rather opaque. Even when it’s your own code, you will sometimes find yourself poking around in it trying to find out what exactly it’s doing.
Tests change that; they light up your code from the inside, and when something goes wrong, they focus light on the part that has gone wrong - even if you hadn’t even realized it had gone wrong.

##Tests make your code more attractive
You might have created a brilliant piece of software, but you will find that many other developers will refuse to look at it because it lacks tests; without tests, they won’t trust it. Jacob Kaplan-Moss, one of Django’s original developers, says “Code without tests is broken by design.”
That other developers want to see tests in your software before they take it seriously is yet another reason for you to start writing tests.

##Tests help teams work together
The previous points are written from the point of view of a single developer maintaining an application. Complex applications will be maintained by teams. Tests guarantee that colleagues don’t inadvertently break your code (and that you don’t break theirs without knowing). If you want to make a living as a Django programmer, you must be good at writing tests!

##Basic testing strategies
There are many ways to approach writing tests.
Some programmers follow a discipline called “test-driven development”; they actually write their tests before they write their code. This might seem counter-intuitive, but in fact it’s similar to what most people will often do anyway: they describe a problem, then create some code to solve it. Test-driven development formalizes the problem in a Python test case.
More often, a newcomer to testing will create some code and later decide that it should have some tests. Perhaps it would have been better to write some tests earlier, but it’s never too late to get started.
Sometimes it’s difficult to figure out where to get started with writing tests. If you have written several thousand lines of Python, choosing something to test might not be easy. In such a case, it’s fruitful to write your first test the next time you make a change, either when you add a new feature or fix a bug.
###Testing in Django
Automated testing is an extremely useful bug-killing tool for the modern Web developer. You can use a collection of tests – a test suite – to solve, or avoid, a number of problems:
* When you’re writing new code, you can use tests to validate your code works as expected.
* When you’re refactoring or modifying old code, you can use tests to ensure your changes haven’t affected your application’s behavior unexpectedly.
Testing a Web application is a complex task, because a Web application is made of several layers of logic – from HTTP-level request handling, to form validation and processing, to template rendering. With Django’s test-execution framework and assorted utilities, you can simulate requests, insert test data, inspect your application’s output and generally verify your code is doing what it should be doing.
The preferred way to write tests in Django is using the unittest module built-in to the Python standard library.

###Writing tests
Django’s unit tests use a Python standard library module: unittest. This module defines tests using a class-based approach.
Here is an example which subclasses from django.test.TestCase, which is a subclass of unittest.TestCase that runs each test inside a transaction to provide isolation:
from django.test import TestCase
from myapp.models import Animal

class AnimalTestCase(TestCase):
    def setUp(self):
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')
When you run your tests, the default behavior of the test utility is to find all the test cases (that is, subclasses of unittest.TestCase) in any file whose name begins with test, automatically build a test suite out of those test cases, and run that suite. 
Where should the tests live?
The default startapp template creates a tests.py file in the new application. This might be fine if you only have a few tests, but as your test suite grows you’ll likely want to restructure it into a tests package so you can split your tests into different submodules such as test_models.py, test_views.py, test_forms.py, etc.  
If your tests rely on database access such as creating or querying models, be sure to create your test classes as subclasses of django.test.TestCase rather than unittest.TestCase.
Using unittest.TestCase avoids the cost of running each test in a transaction and flushing the database, but if your tests interact with the database their behavior will vary based on the order that the test runner executes them. This can lead to unit tests that pass when run in isolation but fail when run in a suite.

###Running tests
Once you’ve written tests, run them using the test command of your project’s manage.py utility:
$ ./manage.py test
Test discovery is based on the unittest module’s built-in test discovery. By default, this will discover tests in any file named “test*.py” under the current working directory.
You can specify particular tests to run by supplying any number of “test labels” to ./manage.py test. Each test label can be a full Python dotted path to a package, module, TestCase subclass, or test method. For instance:
# Run all the tests in the animals.tests module
$ ./manage.py test animals.tests

# Run all the tests found within the 'animals' package
$ ./manage.py test animals

# Run just one test case
$ ./manage.py test animals.tests.AnimalTestCase

# Run just one test method
$ ./manage.py test animals.tests.AnimalTestCase.test_animals_can_speak
You can also provide a path to a directory to discover tests below that directory:
$ ./manage.py test animals/
You can specify a custom filename pattern match using the -p (or --pattern) option, if your test files are named differently from the test*.py pattern:
$ ./manage.py test --pattern="tests_*.py"
If you press Ctrl-C while the tests are running, the test runner will wait for the currently running test to complete and then exit gracefully. During a graceful exit the test runner will output details of any test failures, report on how many tests were run and how many errors and failures were encountered, and destroy any test databases as usual. Thus pressing Ctrl-C can be very useful if you forget to pass the --failfast option, notice that some tests are unexpectedly failing and want to get details on the failures without waiting for the full test run to complete.
If you do not want to wait for the currently running test to finish, you can press Ctrl-C a second time and the test run will halt immediately, but not gracefully. No details of the tests run before the interruption will be reported, and any test databases created by the run will not be destroyed.
Test with warnings enabled
It’s a good idea to run your tests with Python warnings enabled: python -Wa manage.py test. The -Wa flag tells Python to display deprecation warnings. Django, like many other Python libraries, uses these warnings to flag when features are going away. It also might flag areas in your code that aren’t strictly wrong but could benefit from a better implementation.

##The test database
Tests that require a database (namely, model tests) will not use your “real” (production) database. Separate, blank databases are created for the tests.
Regardless of whether the tests pass or fail, the test databases are destroyed when all the tests have been executed.
You can prevent the test databases from being destroyed by using the test --keepdb option. This will preserve the test database between runs. If the database does not exist, it will first be created. Any migrations will also be applied in order to keep it up to date.
As described in the previous section, if a test run is forcefully interrupted, the test database may not be destroyed. On the next run, you’ll be asked whether you want to reuse or destroy the database. Use the test --noinput option to suppress that prompt and automatically destroy the database. This can be useful when running tests on a continuous integration server where tests may be interrupted by a timeout, for example.
The default test database names are created by prepending test_ to the value of each NAME in DATABASES. When using SQLite, the tests will use an in-memory database by default (i.e., the database will be created in memory, bypassing the filesystem entirely!). The TEST dictionary in DATABASES offers a number of settings to configure your test database. For example, if you want to use a different database name, specify NAME in the TEST dictionary for any given database in DATABASES.
On PostgreSQL, USER will also need read access to the built-in postgres database.
Aside from using a separate database, the test runner will otherwise use all of the same database settings you have in your settings file: ENGINE, USER, HOST, etc. The test database is created by the user specified by USER, so you’ll need to make sure that the given user account has sufficient privileges to create a new database on the system.
For fine-grained control over the character encoding of your test database, use the CHARSET TEST option. If you’re using MySQL, you can also use the COLLATION option to control the particular collation used by the test database. See the settings documentation for details of these and other advanced settings.
If using an SQLite in-memory database with SQLite, shared cache is enabled, so you can write tests with ability to share the database between threads.
Finding data from your production database when running tests?
If your code attempts to access the database when its modules are compiled, this will occur before the test database is set up, with potentially unexpected results. For example, if you have a database query in module-level code and a real database exists, production data could pollute your tests. It is a bad idea to have such import-time database queries in your code anyway - rewrite your code so that it doesn’t do this.
This also applies to customized implementations of ready().
See also
The advanced multi-db testing topics.
Order in which tests are executed¶
In order to guarantee that all TestCase code starts with a clean database, the Django test runner reorders tests in the following way:
•	All TestCase subclasses are run first.
•	Then, all other Django-based tests (test cases based on SimpleTestCase, including TransactionTestCase) are run with no particular ordering guaranteed nor enforced among them.
•	Then any other unittest.TestCase tests (including doctests) that may alter the database without restoring it to its original state are run.
Note
The new ordering of tests may reveal unexpected dependencies on test case ordering. This is the case with doctests that relied on state left in the database by a given TransactionTestCase test, they must be updated to be able to run independently.
You may reverse the execution order inside groups using the test --reverse option. This can help with ensuring your tests are independent from each other.
Rollback emulation¶
Any initial data loaded in migrations will only be available in TestCase tests and not in TransactionTestCase tests, and additionally only on backends where transactions are supported (the most important exception being MyISAM). This is also true for tests which rely on TransactionTestCase such as LiveServerTestCase and StaticLiveServerTestCase.
Django can reload that data for you on a per-testcase basis by setting the serialized_rollback option to True in the body of the TestCase or TransactionTestCase, but note that this will slow down that test suite by approximately 3x.
Third-party apps or those developing against MyISAM will need to set this; in general, however, you should be developing your own projects against a transactional database and be using TestCase for most tests, and thus not need this setting.
The initial serialization is usually very quick, but if you wish to exclude some apps from this process (and speed up test runs slightly), you may add those apps to TEST_NON_SERIALIZED_APPS.
To prevent serialized data from being loaded twice, setting serialized_rollback=True disables the post_migrate signal when flushing the test database.
Other test conditions¶
Regardless of the value of the DEBUG setting in your configuration file, all Django tests run with DEBUG=False. This is to ensure that the observed output of your code matches what will be seen in a production setting.
Caches are not cleared after each test, and running “manage.py test fooapp” can insert data from the tests into the cache of a live system if you run your tests in production because, unlike databases, a separate “test cache” is not used. This behavior may change in the future.
Understanding the test output¶
When you run your tests, you’ll see a number of messages as the test runner prepares itself. You can control the level of detail of these messages with the verbosity option on the command line:
Creating test database...
Creating table myapp_animal
Creating table myapp_mineral
This tells you that the test runner is creating a test database, as described in the previous section.
Once the test database has been created, Django will run your tests. If everything goes well, you’ll see something like this:
----------------------------------------------------------------------
Ran 22 tests in 0.221s

OK
If there are test failures, however, you’ll see full details about which tests failed:
======================================================================
FAIL: test_was_published_recently_with_future_poll (polls.tests.PollMethodTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/dev/mysite/polls/tests.py", line 16, in test_was_published_recently_with_future_poll
    self.assertIs(future_poll.was_published_recently(), False)
AssertionError: True is not False

----------------------------------------------------------------------
Ran 1 test in 0.003s

FAILED (failures=1)
A full explanation of this error output is beyond the scope of this document, but it’s pretty intuitive. You can consult the documentation of Python’s unittest library for details.
Note that the return code for the test-runner script is 1 for any number of failed and erroneous tests. If all the tests pass, the return code is 0. This feature is useful if you’re using the test-runner script in a shell script and need to test for success or failure at that level.
Speeding up the tests
Running tests in parallel
As long as your tests are properly isolated, you can run them in parallel to gain a speed up on multi-core hardware. See test --parallel.
Password hashing
The default password hasher is rather slow by design. If you’re authenticating many users in your tests, you may want to use a custom settings file and set the PASSWORD_HASHERS setting to a faster hashing algorithm:
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]
Don’t forget to also include in PASSWORD_HASHERS any hashing algorithm used in fixtures, if any.

