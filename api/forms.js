// One function for both site forms (Hobby plan allows 12 functions per deployment):
// /api/forms?k=nl (weekly e-mail signup, api/_subscribe.js), /api/forms?k=fb («Suggest an improvement», api/_feedback.js). Called directly from src/app.js.
const NL = require('./_subscribe');
const FB = require('./_feedback');
module.exports = (req, res) => ((req.query || {}).k === 'fb' ? FB : NL)(req, res);
