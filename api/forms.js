// One function for both site forms (Hobby plan allows 12 functions per deployment):
// /api/subscribe → ?k=nl (weekly e-mail signup, api/_subscribe.js), /api/feedback → ?k=fb («Suggest an improvement», api/_feedback.js). Rewrites in vercel.json.
const NL = require('./_subscribe');
const FB = require('./_feedback');
module.exports = (req, res) => ((req.query || {}).k === 'fb' ? FB : NL)(req, res);
