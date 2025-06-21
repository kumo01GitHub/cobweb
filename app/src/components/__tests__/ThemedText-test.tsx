import * as React from 'react';
import * as renderer from '@testing-library/react-native';

import { ThemedText } from '../ThemedText';

it(`renders correctly`, () => {
  const tree = renderer.render(<ThemedText>Snapshot test!</ThemedText>).toJSON();

  expect(tree).toMatchSnapshot();
});
