<b>For those who are just starting, I recommend trying out Version1 initially to become acquainted with it.</b>

In Version2
Now we have more rubust functions :

Input Verification:

    The code correctly verifies that the entered secret key and plaintext match before proceeding, which is essential for security.
    It hashes the secret key using SHA-256, ensuring it is 32 bytes (256 bits), which is a good security practice.

Security Best Practices:

    The use of a hashed secret key and the choice of AES encryption are good security practices.
    The code is designed to protect the secret key and ensure that plaintext and secret key entries are validated.

You should always use version2 to en/decrypt your stuff to prevent potential security vulnerabilities

<h2>Please be noted that Version1 and 2 MUST NOT be use interchangeably.</h2>
<h4>Read twice before you impletement anything</h4>
