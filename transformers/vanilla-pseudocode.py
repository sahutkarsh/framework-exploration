    """Transformer variant known as the "vanilla" transformer."""
    x = embedding(enc_inp) * sqrt(d_m)
    x = x + pos_encoding(x)
    x = dropout(x)
    for _ in range(n_enc_layers):
        attn = multi_head_attention(x, x, x, None)
        attn = dropout(attn)
        attn = layer_normalization(x + attn)

        x = pointwise_ff(attn) # GELU activation(affine map(attn))
        x = layer_normalization(x + attn)

    # x is at this point the output of the encoder
    enc_out = x

    x = embedding(dec_inp) * sqrt(d_m)
    x = x + pos_encoding(x)
    x = dropout(x)
    mask = causal_mask(x)
    for _ in range(n_dec_layers):
        attn1 = multi_head_attention(x, x, x, mask)
        attn1 = layer_normalization(attn1 + x)

        attn2 = multi_head_attention(attn1, enc_out, enc_out, None)
        attn2 = dropout(attn2)
        attn2 = layer_normalization(attn1 + attn2)

        x = pointwise_ff(attn2)
        x = layer_normalization(attn2 + x)
    return dense(x)