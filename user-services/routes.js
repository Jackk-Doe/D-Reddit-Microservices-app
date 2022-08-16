const express = require('express');

const UserController = require('./controllers');

const router = express.Router();

router.get('/test', async (req, res) => res.json({ message: 'Testing API Route!' }));

router.get('/:id', UserController.getUser);

router.post('/signup', UserController.signIn);
router.post('/signin', UserController.signUp);

module.exports = router;