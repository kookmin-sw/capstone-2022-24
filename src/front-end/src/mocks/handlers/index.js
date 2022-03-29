import oauth from '@/mocks/handlers/oauth';
import register from '@/mocks/handlers/register';
import user from '@/mocks/handlers/user';

export const handlers = [
	...Object.values(oauth),
	...Object.values(register),
	...Object.values(user),
];
