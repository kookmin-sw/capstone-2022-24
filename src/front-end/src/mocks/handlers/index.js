import oauth from '@/mocks/handlers/oauth';
import register from '@/mocks/handlers/register';
import user from '@/mocks/handlers/user';
import groups from '@/mocks/handlers/groups';
import videos from '@/mocks/handlers/videos';
import mileage from '@/mocks/handlers/mileage';

export const handlers = [
	...Object.values(oauth),
	...Object.values(register),
	...Object.values(user),
	...Object.values(groups),
	...Object.values(videos),
	...Object.values(mileage),
];
