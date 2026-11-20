// One function for the site's forms and accounts (Hobby plan allows 12 functions per deployment), called directly from src/app.js:
// /api/forms?k=nl (weekly e-mail signup, api/_subscribe.js), ?k=fb («Suggest an improvement», api/_feedback.js),
// ?k=login|verify|tg|me|data|logout (accounts and sync, api/_auth.js).
const NL = require('./_subscribe');
const FB = require('./_feedback');
const AUTH = require('./_auth');
module.exports = (req, res) => {
  const k = (req.query || {}).k;
  if (k === 'fb') return FB(req, res);
  if (['login', 'verify', 'tg', 'me', 'data', 'logout'].includes(k)) return AUTH(req, res);
  return NL(req, res);
};
