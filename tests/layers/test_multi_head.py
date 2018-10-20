import unittest
import keras
from keras_bert.layers import get_multi_head_attention


class TestMultiHead(unittest.TestCase):

    def test_sample(self):
        input_layer = keras.layers.Input(
            shape=(512,),
            name='Input',
        )
        embed_layer = keras.layers.Embedding(
            input_dim=12,
            output_dim=768,
            mask_zero=True,
            name='Embedding',
        )(input_layer)
        output_layer = get_multi_head_attention(
            inputs=embed_layer,
            head_num=12,
            name='Multi-Head',
        )
        model = keras.models.Model(inputs=input_layer, outputs=output_layer)
        model.compile(
            optimizer='adam',
            loss='mse',
            metrics=['mse'],
        )
        model.summary()
        self.assertEqual((None, 512, 768), model.layers[-1].output_shape)
