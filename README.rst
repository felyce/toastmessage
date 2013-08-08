Django toast messages
=====================

Provides template tag for displaying toast message for 10 seconds after window load.

Usage
=====

**template.html**::

    <link rel="stylesheet" href="{{ STATIC_URL }}css/jquery.toastmessage.css">
    {% include "toastmessages_fragment.html" %}

    <script src="{{ STATIC_URL }}/js/jquery.toastmessage.js"></script>
    <script type="text/javascript">
        $().toastmessage('showSuccessToast', "Hello there! Message is shown.");
    </script>


