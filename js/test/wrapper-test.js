var test = require('tape');
import {foo} from '../index.js';


test('can import', function (test) {
    test.equal(typeof foo, 'function');
    test.end()
});
