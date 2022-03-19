import { setupWorker } from 'msw';
import { handlers } from '@/mocks/index.js';

export const worker = setupWorker(...handlers);
